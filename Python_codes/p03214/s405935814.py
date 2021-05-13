N=int(input())
A=list(map(int,input().split()))
sum=0
for i in range(N):
  sum+=A[i]
sum
ans=0
for i in range(N):
  A[i]=abs(A[i]*N-sum)
  if(A[i]<A[ans]):
    ans=i
print(ans)