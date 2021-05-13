n = int(input())
lst = list(map(int, input().split()))
for i in range(1, n):
  lst[i] += lst[i - 1]
z = lst[-1]
res = 10 ** 20
for i in range(n - 1):
  res = min(res, abs(lst[i] - (z - lst[i])))
print(res)