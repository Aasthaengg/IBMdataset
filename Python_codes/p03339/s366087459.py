N = int(input())
S =list(input())
ans = N
W = 0
E = S.count('E')

for i in range(N):
    if S[i] =='E':
        E -= 1
    ans = min(ans, W+E)
    if S[i] == 'W':
        W += 1
print(ans)