N,K=map(int,input().split())
*A,=map(int,input().split())
mod=10**9+7

def nC2(n):
  return n*(n-1)//2

inv=0
for i in range(N-1):
  for j in range(i+1,N):
    if A[j]<A[i]: inv += 1
      
inv2=0
B = sorted(A,reverse=True)
for i in range(N-1):
  for j in range(i+1,N):
    if B[j]<B[i]: inv2 += 1

print((inv*K+inv2*nC2(K))%mod)