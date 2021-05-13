import heapq
pop = heapq.heappop
push = heapq.heappush

N, K = list(map(int, input().split()))
V = list(map(int, input().split()))

ans = 0
for i in range(min(N + 1, K + 1)):
  for j in range(min(N + 1, K + 1) - i):
    q = []
    t = 0
    for k in range(i):
      tt = V[k]
      t += tt
      push(q, tt)
    for k in range(j):
      tt = V[N - 1 - k]
      t += tt
      push(q, tt)

    for k in range(K - i - j):
      if q == []:
        break
      tt = pop(q)
      if tt >= 0:
        break
      t -= tt

    ans = max(ans, t)
print(ans)
