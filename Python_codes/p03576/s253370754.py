N, K = map(int, input().split())

P = []
X = []
Y = []

PAppend = P.append
XAppend = X.append
YAppend = Y.append
for i in range(N):
  PAppend([int(x) for x in input().split()])
  XAppend(P[i][0])
  YAppend(P[i][1])

X.sort()
Y.sort()

S = [[0] * N for _ in range(N)]
for i in range(N):
  for j in range(N):
    for k in P:
      if k[0] <= X[i] and k[1] <= Y[j]:
        S[i][j] += 1

ans = float('inf')
for i in range(N - 1):
  for j in range(N - 1):
    for k in range(i + 1, N):
      for l in range(j + 1, N):
        PCount = S[k][l]
        if i > 0:
          PCount -= S[i - 1][l]
        if j > 0:
          PCount -= S[k][j - 1]
        if i > 0 and j > 0:
          PCount += S [i - 1][j - 1]
        if PCount >= K:
          ans = min(ans, (X[k] - X[i]) * (Y[l] - Y[j]))

print(ans)