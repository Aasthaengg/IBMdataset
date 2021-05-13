N, T = map(int, input().split())
A = list(map(int, input().split()))

B = []
Amin = A[0]

for i in range(1, N):
  if A[i] < Amin:
    Amin = A[i]
  else:
    B.append(A[i] - Amin)

result = B.count(max(B))
print(result)