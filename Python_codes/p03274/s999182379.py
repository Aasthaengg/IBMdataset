N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = float('inf')
for i in range(N - K + 1):
    l = X[i]
    r = X[i + K - 1]

    if l >= 0:
        ans = min(ans, abs(r))
    elif r <= 0:
        ans = min(ans, abs(l))
    else:
        ans = min(ans, 2 * abs(r) + abs(l), 2 * abs(l) + abs(r))

print(ans)
