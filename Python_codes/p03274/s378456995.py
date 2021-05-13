N, K = map(int, input().split())
X = list(int(x) for x in input().split())

ans = 10**18
for l in range(N-(K-1)):
    r = l + K - 1
    ans = min(ans, abs(X[l]) + abs(X[r] - X[l]))
    ans = min(ans, abs(X[r]) + abs(X[l] - X[r]))

print(ans)