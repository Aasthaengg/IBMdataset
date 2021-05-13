N, K = map(int, input().split())
X = list(map(int, input().split()))
ans = float("inf")
for i in range(N - K + 1):
    left, right = X[i], X[i + K - 1]
    if left * right <= 0:
        ans = min(ans, abs(left) + right + min(abs(left), right))
    elif left > 0:
        ans = min(ans, right)
    else:
        ans = min(ans, abs(left))
print(ans)
