d,g=map(int,input().split())
p=[0]*d
c=[0]*d
for i in range(d):
  p[i],c[i]=map(int,input().split())
ans=sum(p)
for i in range(1<<d):
  a=[]
  cnt=0
  pt=0
  for j in range(d):
    if (i>>j)&1:
      pt+=p[j]*(j+1)*100+c[j]
      cnt+=p[j]
    else:a+=[(p[j],j+1)]
  if pt<g:
    j,k=a[-1]
    cnt+=(g-pt+k*100-1)//(k*100)
    pt+=k*100*j
  if pt>=g:ans=min(ans,cnt)
print(ans)