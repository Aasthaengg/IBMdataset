x,y=map(int,input().split())
x_=-x
y_=-y
ans=10**9+6
if x<=y:
  ans=min(ans,y-x)
if x_<=y:
  ans=min(ans,y-x_+1)
if x_<=y_:
  ans=min(ans,y_-x_+2)
if x<=y_:
  ans=min(ans,y_-x+1)
print(ans)  