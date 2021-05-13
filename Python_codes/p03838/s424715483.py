x,y=map(int,input().split())
ans=0
if x==0 and y==0:
  print(ans)
  exit(0)
elif y==0:
  if x>0:ans+=1
  ans+=abs(x)
  print(ans)
  exit(0)
elif x==0:
  if y<0:ans+=1
  ans+=abs(y)
  print(ans)
  exit(0)

if x>0 and y>0:
  if x<=y:
    ans+=abs(y-x)
  else:
    ans+=abs(y-x)+2
elif (x>0 and y<0) or (x<0 and y>0):
  ans+=abs(abs(x)-abs(y))+1
elif x<0 and y<0:
  if x<=y:
    ans+=abs(y-x)
  else:
    ans+=abs(y-x)+2
print(ans)