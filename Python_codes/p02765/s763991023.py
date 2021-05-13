N, R = map(int, input().split())
res = 0
if N >= 10:
  res = R
else:
  res = R + 100 * (10 - N)
print(res)