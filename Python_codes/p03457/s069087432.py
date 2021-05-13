N=int(input())
t,x,y=0,0,0
ans="Yes"
for i in range(N):
  T,X,Y=map(int,input().split())
  r=abs(X-x)+abs(Y-y)
  t=T-t
  if r%2!=t%2 or t<r:
    ans="No"
    break
  t=T
  x=X
  y=Y
print(ans)
