import bisect
N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
sumA=[0]
for i in range(N):
  sumA.append(sumA[-1]+A[i])
sumB=[0]
for i in range(M):
  sumB.append(sumB[-1]+B[i])

ans=0
for i in range(N+1):
  k=K-sumA[i]
  if k<0:
    break
  l=bisect.bisect_right(sumB,k)-1
  ans=max(ans,i+l)
print(ans)