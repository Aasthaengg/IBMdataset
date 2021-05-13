n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(m)]
ab.sort(key=lambda x:x[0])
br=set([])
ans=0
now=[0,n+1]
for a,b in ab:
  #print('now',now)
  if now[1]<=a:
    ans+=1
    now=[a,b]
  else:
    now[0]=a
    now[1]=min(now[1],b)
print(ans+1)