n,m,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
if min(y)<=X:
  print("War")
elif Y<=max(x):
  print("War")
else:
  if max(x)>=min(y):
    print("War")
  else:
    print("No War")