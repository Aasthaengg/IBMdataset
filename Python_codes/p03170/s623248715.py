N,K=map(int,input().split())
a=list(map(int,input().split()))
ans=[0 for e in range(K+1)]
for i in range(a[0]):
 ans[i]=1
for m in range(a[0],K+1):
 t=0
 for j in a:
  if j>m:
   continue
  else:
   if ans[m-j]==1:
    t+=1
 if t==0:
  ans[m]=1
 else:
  ans[m]=0
if ans[K]==0:
 print("First")
else:
 print("Second")
