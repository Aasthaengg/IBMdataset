x,y=map(int,input().split())
ans=abs(abs(x)-abs(y))
if x*y<0 or x==0 and y<0 or y==0 and x>0:
  ans+=1
if x*y>0 and y<x:
  ans+=2
print(ans)