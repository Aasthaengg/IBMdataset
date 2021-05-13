n=int(input())
A=list(map(int,input().split()))
r=0
ans=0
sum=0
for l in range(n):
  while r<n and (sum^A[r])==(sum+A[r]):
    sum+=A[r]
    r+=1
  ans+=r-l
  if l == r:
    r+=1
  else:
    sum-=A[l]
print(ans)
