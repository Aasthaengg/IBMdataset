import heapq

N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
Used = [1] * M
Q = []

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, c, _))
    Edge[b].append((a, c, _))

for i in range(N):
    now = (0, i)
    Seen = [-1] * N
    used = [-1] * N
    wait = []
    heapq.heappush(wait, now)
    Seen[i] = 0
    while len(wait) > 0:
        time, now = heapq.heappop(wait)
        for nex, cost, bridgenum in Edge[now]:
            if Seen[nex] == -1:
                Ne = (time + cost, nex)
                Seen[nex] = time + cost
                heapq.heappush(wait, Ne)
                used[nex] = bridgenum
            elif Seen[nex] > time + cost:
                Ne = (time + cost, nex)
                Seen[nex] = time + cost
                heapq.heappush(wait, Ne)
                used[nex] = bridgenum
    for j in range(N):
        if used[j] != -1:
            Used[used[j]] = 0
print(sum(Used))