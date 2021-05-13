import heapq
N, K = map(int, input().split())
S = [[] for _ in range(N)]
E = [0] * N
Q = []
D = []
x = 0
k = 0
h = 0
for i in range(N):
  t, d = map(int, input().split())
  S[i] = [d, t]
S.sort(reverse=True)
for d, t in S:
  if E[t - 1] > 0:
    D.append(d)
  elif k < K:
    E[t - 1] += 1
    heapq.heappush(Q, d)
    x += 1
    k += 1
    h += d
h += x ** 2
for d in D:
  if k < K:
    heapq.heappush(Q, d)
    h += d
    k += 1
    continue
  q = heapq.heappop(Q)
  if d <= q:
    break
  _h = h - q - x ** 2 + d + (x - 1) ** 2
  if _h < h:
    break
  heapq.heappush(Q, d)
  x -= 1
  h = _h
print(h)