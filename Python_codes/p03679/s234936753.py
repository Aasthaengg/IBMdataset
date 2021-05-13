X, A, B = map(int, input().split())
if A >= B:
  print("delicious")
else:
  if X + A >= B:
    print("safe")
  else:
    print("dangerous")