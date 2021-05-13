n,m=map(int, input().split())
alist=[0]*(m+1)
for i in range(n):
  blist=list(map(int, input().split()))
  for j in range(blist[0]):
    alist[blist[j+1]]+=1
cnt=0
for i in range(m+1):
  if alist[i]==n:
    cnt+=1
print(cnt)