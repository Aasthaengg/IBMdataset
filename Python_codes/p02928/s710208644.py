n,k=map(int,input().split())
a=list(map(int,input().split()))
t1=[0]*n
t2=[0]*n
for i in range(n):
  for j in range(n):
    if a[i]>a[j]:
      t1[i]=t1[i]+1
      if i<j:
        t2[i]=t2[i]+1
ans=0
for i in range(n):
  ans=(ans+k*t2[i]+(k*(k-1)*t1[i])//2)%(10**9+7)
print(ans)