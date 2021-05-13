import heapq

N, K = map(int, input().split())

td = []
for _ in range(N):
    t, d = map(int, input().split())
    td.append((t, d))

td.sort(reverse=True, key=lambda x: x[1])

g1 = [0] * (N + 1)
g0 = []
sumt = 0
for i in range(K):
    t, d = td[i]
    if g1[t] == 0:
        g1[t] = d
        sumt += 1
    elif g1[t] < d:
        heapq.heappush(g0, g1[t])
        g1[t] = d
    else:
        heapq.heappush(g0, d)

sumg1 = sum(g1)
sumg0 = sum(g0)
ans = sumg1 + sumg0 + sumt * sumt
for i in range(K, N):
    t, d = td[i]
    if g1[t] == 0 and len(g0) > 0:
        g1[t] = d
        sumg1 += d
        sumg0 -= heapq.heappop(g0)
        sumt += 1
        newans = sumg1 + sumg0 + sumt * sumt
        ans = max(ans, newans)

print(ans)