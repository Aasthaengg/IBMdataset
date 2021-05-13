a, b, c = map(int, input().split())
k = a-b
vv = c - k
if vv >= 0:
  print(vv)
else:
  print(0)