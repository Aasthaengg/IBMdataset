n,m,x,y=[int(_) for _ in input().split()]
X=[int(_) for _ in input().split()]
Y=[int(_) for _ in input().split()]

ans="No War"
if max(X)>=min(Y):
  ans="War"
if not(x<=max(X)<y):
  ans="War"
print(ans)