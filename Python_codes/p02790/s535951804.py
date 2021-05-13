a, b = map(int,input().split())
a1, b1 = str(a) * b, str(b) * a
ans = min(a1[0],b1[0])
if int(ans) == b:
  print(b1)
else:
  print(a1)