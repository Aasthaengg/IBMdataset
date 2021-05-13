N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = float('inf')
for l in range(N - K + 1):
    r = l + K - 1

    if X[l] < 0 and X[r] <~ 0:
        ans = min(ans, abs(X[l]))
    elif X[l] >= 0 and X[r] > 0:
        ans = min(ans, X[r])
    else:
        ans = min(ans, abs(X[l]) + X[r] + min(abs(X[l]), X[r]))


print(ans)