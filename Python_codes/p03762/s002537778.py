mod=1000000007
N,M=map(int,input().split())
s=0
k=0
L=list(map(int,input().split()))
R=list(map(int,input().split()))
for i in range(N):
  s+=L[i]*(2*i-N+1)
for j in range(M):
  k+=R[j]*(2*j-M+1)
print((k%mod*s%mod)%mod)