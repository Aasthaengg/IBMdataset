from heapq import heappush, heappop
from collections import defaultdict

N, K = map(int, input().split())
TD = []

sushi = []
kinds = []


for i in range(N):
  t, d = map(int, input().split())
  sushi.append((d, t))
  kinds.append(t)

sushi.sort(key=lambda x: x[0], reverse=True)
sushidict = defaultdict(int)
kind_all = len(set(kinds))

cnt = 0
sushiq = []

for i in range(K):
  d, t = sushi[i]
  heappush(sushiq, (d, t))
  sushidict[t] += 1
  cnt += d

n_kind = len(sushidict)
res = []
res.append(cnt+n_kind**2)

for i in range(K, N):
  d, t = sushi[i]

  if sushidict[t] > 0:
    continue

  d_min, t_min = heappop(sushiq)
  while sushidict[t_min] == 1 and sushiq:
    d_min, t_min = heappop(sushiq)

  if not sushiq:
    break

  sushidict[t_min] -= 1
  sushidict[t] += 1
  n_kind += 1
  cnt = cnt - d_min + d

  res.append(cnt+n_kind ** 2)
  if n_kind == kind_all:
    break

print(max(res))