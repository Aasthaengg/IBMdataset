X, A, B = map(int, input().split())
s = 0
if s-A+B <= s:
  print("delicious")
elif s-A+B > s and s-A+B < X+1:
  print("safe")
else:
  print("dangerous")