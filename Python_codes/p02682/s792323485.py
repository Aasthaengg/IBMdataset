a, b, c, k = map(int, input().split())
res = 0
if k <= a :
  res = k
  print(res)
else:
  if b >= k-a:
    res = a
    print(res)
  elif b < k-a:
    res = a - (k-b-a)
    print(res)