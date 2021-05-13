n,m,x,y=list(map(int,input().split()))
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
ans='War'
for i in range(x+1,y):
  if max(X)<i and i<=min(Y):
    ans='No War'
print(ans)