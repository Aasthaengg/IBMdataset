x,a,b = list(map(int,input().strip().split()))

if abs(a-x) > abs(b-x):
  print("B")
else:
  print("A")