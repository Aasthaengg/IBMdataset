N, M = map(int, input().split())
A = [[] for _ in range(8)]
for _ in range(N):
  a = list(map(int, input().split()))
  for k in range(8):
    S = 0
    tmp = k
    L = [(k // 4) % 2, (k // 2) % 2, k % 2]
    for j in range(3):
      S += a[j] * ((-1) ** L[j])
    A[k].append(S)
for i in range(8):
  A[i].sort(reverse=True)
X = [sum(A[i][:M]) for i in range(8)]
print(max(X))