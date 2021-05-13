from math import ceil
N = int(input())
result = 10 ** 6
for i in range(1, ceil(N / 2) + 1):
  a = str(i)
  b = str(N - i)
  result = min(result, sum(map(int, a)) + sum(map(int, b)))
print(result)
