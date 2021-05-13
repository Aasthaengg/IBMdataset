import sys
from itertools import combinations as combi
input = sys.stdin.readline
H, W, K = map(int, input().split())
S = [list(map(int, list(input())[: -1])) for _ in range(H)]
res = H + W - 2
for t in range(H):
  for c in combi([x for x in range(1, H)], t):
    s = set(c)
    table = [0] * (t + 1)
    rres = t + 0
    for x in range(W):
      i = 0
      y = 0
      while y < H:
        if y in s: i += 1
        table[i] += S[y][x]
        y += 1
        if table[i] > K: break
      else: continue
      rres += 1
      table = [0] * (t + 1)
      i = 0
      y = 0
      while y < H:
        if y in s: i += 1
        table[i] += S[y][x]
        y += 1
        if table[i] > K: break
      else: continue
      rres = H + W - 2
      break

    #print(c, rres, table)
    res = min(res, rres)
print(res)