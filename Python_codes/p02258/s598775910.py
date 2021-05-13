n = int(input())

max_diff = - 10 ** 9
min_n = int(input())

for i in range(1, n):
  n = int(input())
  max_diff = max(max_diff, n - min_n)
  min_n = min(min_n, n)

print(max_diff)