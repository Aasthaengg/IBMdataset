N = int(input())
A = input().split()

B = []
for i in range(N-1, -1, -2):
  B.append(A[i])

for j in range(N % 2, N, 2):
  B.append(A[j])

print(" ".join(B))