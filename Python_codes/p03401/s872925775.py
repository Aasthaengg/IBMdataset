n = int(input())
A = list(map(int, input().split()))

A = [0] + A + [0]
C = [0]
for i in range(1, n+2):
  C.append(C[-1] + abs(A[i] - A[i-1]))

for i in range(1, n+1):
  dist = C[i-1] + C[-1] - C[i+1] + abs(A[i+1] - A[i-1])
  print(dist)