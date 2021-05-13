n=int(input())
a=list(map(int,input().split()))
a.sort()
lb=0
ub=3*n-1
ans=0
for i in range(n):
  lb+=1
  ub-=1
  ans+=a[ub]
  ub-=1
print(ans)