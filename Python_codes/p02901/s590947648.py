N, M = map(int, input().split())
bit = [int(1e18) for _ in range(1 << N)]
bit[0] = 0
F = {0}
for _ in range(M):
  a, b = map(int, input().split())
  c = list(map(int, input().split()))
  bas = 0
  for k in range(b):
    c[k] -= 1
    bas += (1 << c[k])
  L = [[j, bit[j]] for j in F]
  for j in L:
    tb = 0
    for k in range(N):
      tb += (((j[0] >> k) & 1) | ((bas >> k) & 1)) << k
    bit[tb] = min(bit[tb], j[1] + a)
    F.add(tb)
if bit[-1] != int(1e18):
  print(bit[-1])
else:
  print(-1)