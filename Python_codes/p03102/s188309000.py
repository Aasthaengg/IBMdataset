N,M,H=list(map(int,input().split()))
B=list(map(int,input().split()))
count=0
for i in range(N):
  A=list(map(int,input().split()))
  ans=0
  for k in range(M):
    ans+=A[k]*B[k]
  if ans+H>0:
    count+=1
print(count)
