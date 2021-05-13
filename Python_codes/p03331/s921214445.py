n = int(input())
res = 10000
for i in range(1, n // 2 + 1):
  s = str(i)
  t = str(n - i)
  cnt = 0
  for j in s + t:
    cnt += int(j)
  res = min(res, cnt)
print(res)