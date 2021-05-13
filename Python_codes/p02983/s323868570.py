l, r = map(int, input().split())

if l + 2019 <= r:
  print(0)
else:
  res = []
  for i in range(l, r+1):
     for j in range(i+1, r+1):
        res.append((i*j)%2019)
  print(min(res))