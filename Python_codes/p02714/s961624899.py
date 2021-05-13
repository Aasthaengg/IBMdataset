N = int(input())
S = input()
r = S.count('R')
g = S.count('G')
b = S.count('B')
ans = r*g*b
for x in range(N):
    for a in range(N):
        y = x+a
        z = y+a
        if z >= N:
            continue
        if S[x] == S[y]:
            continue
        if S[y] == S[z]:
            continue
        if S[x] == S[z]:
            continue
        ans = ans-1
print(ans)