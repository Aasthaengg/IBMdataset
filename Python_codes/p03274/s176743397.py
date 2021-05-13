N, K = map(int, input().split())
x = list(map(int, input().split()))
ans = float("inf")
for i in range(N - K + 1):
    left = x[i]
    right = x[K - 1 + i]
    if left * right >= 0:
        ans = min(ans, max(abs(left), abs(right)))
    else:
        ans = min(ans, min(abs(left), abs(right)) + abs(left - right))
print(ans)