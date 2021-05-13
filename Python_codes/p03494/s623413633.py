n=int(input())
a=list(map(int,input().split()))
ans=float('inf')
for i in range(n):
  res=0
  while a[i]%2==0:
    a[i]/=2
    res+=1
  ans=min(ans,res)
print(ans)