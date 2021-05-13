n=int(input())
a=[0]+list(map(int,input().split()))+[0]

dist=[]

for i in range(len(a)-1):
  dist.append(abs(a[i+1]-a[i]))
  
xxx=sum(dist)

for i in range(n):
  ans=xxx
  ans-=dist[i]
  ans-=dist[i+1]
  ans+=abs(a[i+2]-a[i])
  print(ans)