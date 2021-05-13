n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x_sum, y_sum = 0, 0
for i in range(n):
  k = i + 1
  x_sum += (2*k - n - 1) * x[i]
  x_sum = x_sum % 1000000007
for i in range(m):
  k = i + 1
  y_sum += (2*k - m - 1) * y[i]
  y_sum = y_sum % 1000000007
ans = (x_sum * y_sum) % 1000000007
print(ans)