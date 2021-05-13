X,A,B=map(int,input().split())
if B<=A:
  print("delicious")
elif B>A and (A+X)>=B:
  print("safe")
else:
  print("dangerous")