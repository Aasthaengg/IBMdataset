N = int(input())
abc = [list(map(int,input().split())) for _ in range(N)]

A = [0]*N
B = [0]*N
C = [0]*N

for i,[a,b,c] in enumerate(abc):
  if i == 0:
    A[0],B[0],C[0] = a,b,c
  else:
    A[i] = max((B[i-1]+a),(C[i-1]+a))
    B[i] = max((A[i-1]+b),(C[i-1]+b))
    C[i] = max((A[i-1]+c),(B[i-1]+c))
  
print(max(A[-1],B[-1],C[-1]))