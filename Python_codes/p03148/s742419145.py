import heapq

N, K = map(int, input().split())
dt = [list(map(int, input().split()))[::-1] for i in range(N)]
dt.sort(reverse=True)

ans = 0
t_set = set()
candidates = []
for d, t in dt[:K]:
  if t in t_set:
    heapq.heappush(candidates, [d, t])
    ans += d
  else:
    t_set.add(t)
    ans += d

x = len(t_set)
ans += x**2

if len(candidates) == 0:
  print(ans)
  quit()

ans = [ans]
for d, t in dt[K:]:
  if t in t_set:
    continue
  cand_d, cand_t = heapq.heappop(candidates)
  _ans = ans[-1] - cand_d + d + (2*x+1)
  x += 1
  ans.append(_ans)
  t_set.add(t)
  if len(candidates) == 0:
    break

print(max(ans))