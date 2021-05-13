W,a,b = [int(i) for i in input().split()]
if a <= b and b <= a + W:
  print(0)
else:
  print(abs(a-b)-W)