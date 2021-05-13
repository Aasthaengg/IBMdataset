N, M, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
x = [0 for i in range(N+1)]
for i in range(M):
  x[A[i]] = 1
ans1 = 0
for i in range(0,X):
  ans1 += x[i]
ans2 = 0
for i in range(X,N):
  ans2 += x[i]
print(min(ans1, ans2))