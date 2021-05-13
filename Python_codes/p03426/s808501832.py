H, W, D = map(int, input().split())
peak = H * W
L = [[0 for j in range(i+1, peak+1, D)] for i in range(D)]
dd = {}
for i in range(H):
  line = list(map(int, input().split()))
  for j in range(W):
    dd[line[j]] = [i, j]
for m in range(D):
  ddd = (peak - m - 1) // D
  for k in range(1, ddd + 1):
    dist = abs(dd[k*D+m+1][0] - dd[(k-1)*D+m+1][0])
    dist += abs(dd[k*D+m+1][1] - dd[(k-1)*D+m+1][1])
    L[m][k] = L[m][k-1] + dist
Q = int(input())
for i in range(Q):
  pL, pR = map(int, input().split())
  l, r = (pL - 1) // D, (pR - 1) // D
  mod = (pL - 1) % D
  print(L[mod][r] - L[mod][l])