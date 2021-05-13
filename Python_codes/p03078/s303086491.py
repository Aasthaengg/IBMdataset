x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = [0] * (x * y)
for i in range(x):
  for j in range(y):
    D[i * y + j] = A[i] + B[j]
D.sort(reverse=True)
E = [0] * (z * k)
size = min(x * y, k)
for i in range(z):
  for j in range(size):
    E[i * size + j] = C[i] + D[j]
E.sort(reverse=True)
print(*E[:k], sep='\n')