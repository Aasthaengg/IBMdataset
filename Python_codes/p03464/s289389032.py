K = int(input())
A = [int(x) for x in input().split()]
C = [[0, 0] for _ in range(K + 1)]
C[K] = [2, 2]
for i in range(K - 1, -1, -1):
  C[i][0] = A[i] * -(-C[i + 1][0] // A[i])
  C[i][1] = A[i] * (C[i + 1][1] // A[i]) + (A[i] - 1)
  if C[i][0] > C[i + 1][1]:
    print(-1)
    break
else:
  print(C[0][0], C[0][1])