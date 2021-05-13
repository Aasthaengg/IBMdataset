A = list(map(int, input().split()))
A.sort()

ans = A[2] - A[1]

if (A[1] - A[0]) % 2 == 0:
  print(ans + (A[1] - A[0]) // 2)
else:
  print(ans + (A[1] - A[0] + 1) // 2 + 1)

