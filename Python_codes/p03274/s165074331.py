N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = 10**18
for i in range(N - K + 1):
    d1 = X[i + K - 1] - X[i] + abs(X[i])
    d2 = X[i + K - 1] - X[i] + abs(X[i + K - 1])
    # print('d', d)
    ans = min(ans, d1, d2)
print(ans)
