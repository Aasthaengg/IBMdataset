import sys
input = sys.stdin.readline
H, W = map(int, input().split())
S = [list(input())[: -1] for _ in range(H)]

imoslr = [[0] * (W + 1) for _ in range(H)]
for i in range(H):
  c = 0
  prev = 0
  for j in range(W):
    if S[i][j] == "#":
      imoslr[i][j] -= c
      imoslr[i][prev] += c
      prev = j + 1
      c = 0
    else: c += 1
  imoslr[i][prev] += c
  for j in range(W): imoslr[i][j + 1] += imoslr[i][j]

imosud = [[0] * (W) for _ in range(H + 1)]
for i in range(W):
  c = 0
  prev = 0
  for j in range(H):
    if S[j][i] == "#":
      imosud[j][i] -= c
      imosud[prev][i] += c
      prev = j + 1
      c = 0
    else: c += 1
  imosud[prev][i] += c
  for j in range(H): imosud[j + 1][i] += imosud[j][i]

res = 0
for i in range(H):
  for j in range(W): res = max(res, imoslr[i][j] + imosud[i][j] - 1)
print(res)