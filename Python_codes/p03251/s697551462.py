n,m,x,y = map(int,input().split())
X = [int(i) for i in input().split()]
Y = [int(i) for i in input().split()]
a = max(max(X),x)
b = min(min(Y),y)
if(a < b):
  print("No War")
else:
  print("War")