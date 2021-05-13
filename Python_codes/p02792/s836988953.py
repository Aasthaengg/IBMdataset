N = int(input())
A = [[0 for i in range(9)] for j in range(9)]
i = 92838
for i in range(1, N+1):
  if i % 10 != 0:
    A[int(str(i)[0])-1][i % 10 - 1] += 1
ans = 0
for i in range(9):
  for j in range(9):
    ans += A[i][j] * A[j][i]
print(ans)