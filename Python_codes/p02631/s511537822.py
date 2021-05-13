N = int(input())
A = [int(n) for n in input().split()]
X = 0
ans = []
for i in range(N):
  X = X^A[i]
for i in range(N):
  ans.append(X^A[i])
print(*ans)