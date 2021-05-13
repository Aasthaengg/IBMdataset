A,B,C = (int(x) for x in input().split())
v = A-B
if C-v >= 0:
  print(C-v)
else:
  print(0)