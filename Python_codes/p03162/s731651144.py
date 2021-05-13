import sys
N = int(input())
X = [[0,0,0]] + [list(map(int, input().split())) for _ in range(N)]
A = [[0]*3 for _ in range(N+1)]
for i in range(1,N+1):
  A[i][0] = max(A[i-1][1],A[i-1][2]) + X[i][0]
  A[i][1] = max(A[i-1][0],A[i-1][2]) + X[i][1]
  A[i][2] = max(A[i-1][0],A[i-1][1]) + X[i][2]

print(max(A[N]))