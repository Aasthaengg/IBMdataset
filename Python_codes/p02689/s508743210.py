from collections import defaultdict
n,m=map(int,input().split())
h=list(map(int,input().split()))
ma=[0 for _ in range(n)]
for _ in range(m):
  a,b=map(int,input().split())
  ma[a-1]=max(ma[a-1],h[b-1])
  ma[b-1]=max(ma[b-1],h[a-1])
cnt=0
for i,hh in enumerate(ma):
  if h[i] > hh:
    cnt+=1
print(cnt)
  
