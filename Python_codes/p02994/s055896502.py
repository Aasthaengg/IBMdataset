n, l = map(int, input().split())


a = []
res = 300
for i in range(n):
  a.append(l+i)
  res = min(res, abs(l+i))
s = sum(a)
if res in a:
  print(s-res)
else:
  print(s+res)