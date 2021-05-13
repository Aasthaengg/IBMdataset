N, C = map(int, input().split())
S = [[0, 0, 0] for i in range(N + 2)]
L = [[0, 0, 0] for i in range(N + 2)]
R = [[0, 0, 0] for i in range(N + 2)]
for i in range(N):
  x, v = map(int, input().split())
  S[i + 1] = [v, x, C - x]
  L[i + 1][0] = L[i][0] - x + S[i][1] + v
  L[i + 1][1] = L[i + 1][0] - x
  L[i + 2][2] = max(L[i + 1][2], L[i + 1][1])
for i in range(N, 0, -1):
  R[i][0] = R[i + 1][0] - S[i][2] + S[i + 1][2] + S[i][0]
  R[i][1] = R[i][0] - S[i][2]
  R[i - 1][2] = max(R[i][2], R[i][1])
ans = 0
for i in range(N + 1):
  ans = max(L[i][0] + R[i][2], L[i][2] + R[i][0], ans)
print(ans)