n, k = map(int, input().split())
x = list(map(int, input().split()))
ans = 10**10
for i in range(n - k + 1):
  ans = min(ans, max(0, -x[i]) + max(0, 2 * x[i + k - 1]),
            max(0, -2 * x[i]) + max(0, x[i + k - 1]))
print(ans)
