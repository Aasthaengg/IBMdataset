N = int(input())
A = list(map(int, input().split()))
B = [[0 for i in range(N)]for j in range(60)]
M = 1000000007
ans = [0 for i in range(60)]
sumB = [[0 for i in range(N)]for j in range(60)]
for j in range(N):
  for i in range(60):
    B[i][j] = A[j]>>i & 1
    sumB[i][j] = A[j]>>i & 1
    if j > 0:
      sumB[i][j] += sumB[i][j-1]
for i in range(1, N):
  for j in range(60):
    if B[j][-i]==0:
      ans[j] += sumB[j][-(i+1)]
    else:
      ans[j] += N-i-sumB[j][-(i+1)]
a = 0
for i in range(60):
  a += (ans[i]*pow(2, i, M))%M
  a %= M
print(a)