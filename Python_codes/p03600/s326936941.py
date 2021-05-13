N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

INF = 10 ** 15
B = [[INF for _ in range(N)] for _ in range(N)]

for k in range(N):
  for i in range(N):
    for j in range(N):
      B[i][j] = min(B[i][j], A[i][k] + A[k][j])
#print("B:", B)

for i in range(N):
  if A[i] != B[i]:
    print(-1)
    exit()
    
C = [[1 for _ in range(N)] for _ in range(N)]
for i in range(N):
  for j in range(i + 1, N):
    for k in range(N):
      if i != k and j != k:
        if A[i][k] + A[k][j] == A[i][j]:
          C[i][j] = 0
#print("C:", C)   

answer = 0
for i in range(N):
  for j in range(i + 1, N):
    answer += C[i][j] * A[i][j]
print(answer)