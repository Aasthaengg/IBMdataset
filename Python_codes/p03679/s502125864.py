X,A,B = map(int,input().split())
if A >= B:
  print("delicious")
else:
  if B-A <= X:
    print("safe")
  else:
    print("dangerous")