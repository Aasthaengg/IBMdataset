mod=10**9+7

N=int(input())
T=list(map(int,input().split()))
A=list(map(int,input().split()))

B=[]
C=[]
B.append([0,T[0],T[0]])
C.append([N-1,A[-1],A[-1]])

if N>1:
  for i in range(1,N):
    B.append([i,T[i],T[i] if T[i]>T[i-1] else 1])
  for i in range(N-2,-1,-1):
    C.append([i,A[i],A[i] if A[i]>A[i+1] else 1])
C.sort()
#print(B)
#print(C)

ans=1
for i in range(N):
  d=min(B[i][1],C[i][1])-max(B[i][2],C[i][2])+1
  ans*=d if d>=0 else 0
  ans%=mod
print(ans)