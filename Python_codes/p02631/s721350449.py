N=int(input())
A=list(map(int, input().split()))
S=A[0]
for i in range(N-1):
  S=S^A[i+1]
L=[0]*N
for i in range(N):
  L[i]=A[i]^S
print(*L)
