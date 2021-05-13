N = int(input())
S = input()

i = 0
ans = 0
while i + 2 < N:
    s = i
    e = i + 3
    if S[s:e] == 'ABC':
        ans += 1
        i += 3
    else:
        i += 1
print(ans)