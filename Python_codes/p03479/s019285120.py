x,y=map(int,input().split())
ans=1
tmp=x
while 1:
  if tmp*2<=y:
    ans+=1
    tmp*=2
  else:
    print(ans)
    exit()