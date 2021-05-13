N,M=map(int,input().split())

l=[]
for i in range(M):
  l.append(list(map(int,input().split()))[1:])

p=list(map(int,input().split()))

ans=0
for i in range(2**N):
  isOK=True
  for j in range(M):
    stat=0
    for k in l[j]:
      k-=1
      if i&(1<<k):
        stat=(stat+1)%2
    if stat!=p[j]:
      isOK=False
  if isOK:
    ans+=1
print(ans)