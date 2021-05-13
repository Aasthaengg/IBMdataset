from collections import defaultdict
n,m=map(int,input().split())
h=list(map(int,input().split()))
dd=defaultdict(set)
for i in range(m):
  a,b=map(int,input().split())
  dd[a-1].add(b-1)
  dd[b-1].add(a-1)
cnt=0
for i,hh in enumerate(h):
  flg=True
  for j in dd[i]:
    if hh <= h[j]:
      flg=False
      break
  if flg:
    cnt+=1
print(cnt)
  
