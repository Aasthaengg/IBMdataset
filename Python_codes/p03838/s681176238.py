x,y=map(int,input().split())
ans=abs(y)-abs(x)
if x*y<0:ans=abs(ans)+1
if x*y==0:
  if x<y:ans=y-x
  elif x>y:ans=abs(ans)+1
elif ans>0:
  if x<0 and y<0:ans+=2
elif ans<0:
  if x>0 and y>0:ans=abs(ans)+2
  else:ans=abs(ans)
print(ans)