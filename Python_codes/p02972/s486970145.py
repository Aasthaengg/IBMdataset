N=int(input())
a=list(map(int,input().split()))
b=[]
dp=[0]*(N+1)
ans=0
for i in range(N,0,-1):
  p=0
  for j in range(1,N//i+1):
    p+=dp[j*i]
  if p%2!=a[i-1]:
    dp[i]=1
    ans+=1
    b.append(i)
b.sort()
print(ans)
print(*b)