N = int(input())
S = list(input())
ans = 0
for i in range(N):
    X = set(S[:i])
    Y = set(S[i:])
    tmp = len(X & Y)
    ans = max(ans, tmp)

print(ans)
