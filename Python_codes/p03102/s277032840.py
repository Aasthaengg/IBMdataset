n,m,c=map(int, input().split())
blist=list(map(int, input().split()))
ans=0
for i in range(n):
  alist=list(map(int, input().split()))
  cnt=0
  for i in range(m):
    cnt+=alist[i]*blist[i]
  if cnt>-c:
    ans+=1
print(ans)