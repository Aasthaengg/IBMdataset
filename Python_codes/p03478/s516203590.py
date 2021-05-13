N,a,b=list(map(int,input().split()))
ans=0
for i in range(1,N+1):
  h=i
  sum=0
  while i>0:
    sum+=i%10
    i=i//10
  if sum<=b and a<=sum:
    ans+=h
print(ans)