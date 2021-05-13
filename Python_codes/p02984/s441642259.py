import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))

R = [0] * N
R[0] = sum(A)
for i in range(1, len(A), 2):
  R[0] -= A[i] * 2

for i in range(len(A)-1):
  R[i + 1] = A[i] * 2 - R[i]
  
print(*R)