a,b=map(int,input().split())

if b==1:
  print(0)
if b>1:
  x=a
  ans=1
  while x<b:
    ans+=1
    x+=a-1
  print(ans)