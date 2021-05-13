N,M,X = map(int, input().split())
A = list(map(int, input().split()))
B = []
C = []
for i in range(0, X):
  if i in A:
    B.append(i)
for j in range(X, N):
  if j in A:
    C.append(j)
print(min(len(B), len(C)))