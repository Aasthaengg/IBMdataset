N, C = map(int, input().split())
XV = [list(map(int, input().split())) for _ in range(N)]

R = [[0 for _ in range(4)] for _ in range(N)]
L = [[0 for _ in range(4)] for _ in range(N)]

for i in range(N):
  R[i][3] = 0
  L[i][3] = 0

for i in range(N):
  R[i][0] = XV[i][0]
  R[i][1] = XV[i][1]
  L[i][0] = C - XV[i][0]
  L[i][1] = XV[i][1]
L.sort()

for i in range(N):
  R[i][2] = R[i - 1][2] + R[i][1]
  L[i][2] = L[i - 1][2] + L[i][1]
for i in range(N):
  R[i][2] -= R[i][0]
  L[i][2] -= L[i][0] 
  R[i][3] = max(R[i - 1][3], R[i][2])
  L[i][3] = max(L[i - 1][3], L[i][2])
#print("R:", R)
#print("L:", L)

answer = []
for i in range(N):
  if i != N - 1:
    answer.append(R[i][2] + max(L[N - 2 - i][3] - R[i][0], 0))
  else:
    answer.append(R[i][2])

L, R = R, L
for i in range(N):
  if i != N - 1:
    answer.append(R[i][2] + max(L[N - 2 - i][3] - R[i][0], 0))
  else:
    answer.append(R[i][2])

answer = max(answer)
print(answer if answer > 0 else 0)