import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))

A = sorted(A)

cur = 0
ng = 0
for i in range(N):
  if A[i] > cur * 2:
    ng = i
  cur += A[i]
  
print(N - ng)