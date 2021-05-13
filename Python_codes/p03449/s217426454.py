N = int(input())
A = []
for i in range(2):
  A.append(list(map(int, input().split())))
X = A[0][0] + sum(A[1])
ans = X
for i in range(N-1):
  X = X - A[1][i] + A[0][i+1]
  ans = max(ans, X)
print(ans)