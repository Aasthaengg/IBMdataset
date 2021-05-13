K,N=map(int,input().split())
A=list(map(int,input().split()))
temp=10**9
for i in range(N-1):
  temp=min(temp,A[i]+K-A[i+1])

print(min(A[-1]-A[0],temp))