N = int(input())
S = input()
ans = 0
for i in range(1, N):
    X = set(S[:i])
    Y = set(S[i:])
    ans = max(ans, len(X & Y))
print(ans)