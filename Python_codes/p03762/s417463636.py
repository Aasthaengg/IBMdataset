n, m = map(int, input().split())
list_x = list(map(int, input().split()))
list_y = list(map(int, input().split()))

sum_x_pair = 0
for i in range(n):
  sum_x_pair += i * list_x[i] - (n - i - 1) * list_x[i]
sum_y_pair = 0
for j in range(m):
  sum_y_pair += j * list_y[j] - (m - j - 1) * list_y[j]

print((sum_x_pair * sum_y_pair) % (7 + 10**9))