import sys
input = sys.stdin.readline
H, W, A, B = map(int, input().split())
res = [[0] * W for _ in range(H)]
for i in range(B):
  for j in range(A): res[i][j] = 1
for i in range(B, H):
  for j in range(A, W): res[i][j] = 1
for r in res: print("".join(list(map(str, r))))