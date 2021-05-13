N, M = map(int,input().split())
A = list(map(int,input().split()))
a = 0
for i in range(M):
  a += A[i - 1]
b = N - a
if b < 0:
  print(-1)
else:
  print(b)