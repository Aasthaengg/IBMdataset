X, A, B = map(int,input().split())
L = A + X
if A >= B:
  print("delicious")
elif B <= L:
  print("safe")
else:
  print("dangerous")
