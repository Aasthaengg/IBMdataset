import sys
readline = sys.stdin.readline

N = int(readline())
A = [0] * N
B = [0] * N
C = [0] * N
for i in range(N):
  A[i],B[i] = map(int,readline().split())
  C[i] = (A[i] + B[i], i)
  
C = sorted(C, key = lambda x:x[0], reverse = True)

ans = 0
for i in range(len(C)):
  if i % 2 == 0:
    ans += A[C[i][1]]
  else:
    ans -= B[C[i][1]]
    
print(ans)