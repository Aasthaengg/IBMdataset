n=int(input())
x=list(map(int,input().split()))

ans=float('inf')

for i in range(1, 100):
  res=0
  for j in range(n):
    res+=(x[j]-i)**2
  ans=min(res,ans)
print(ans)