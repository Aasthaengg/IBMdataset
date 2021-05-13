import heapq

N, M, R = map(int, input().split())
D = [int(a) - 1 for a in input().split()]
D.sort()
Dtod = {}
dtoD = {}
Dest = set()
for i, d in enumerate(D):
    Dtod[d] = i
    dtoD[i] = d
    Dest.add(d)
Map = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Map[a].append((b, c))
    Map[b].append((a, c))

Roots = [[float('inf')] * R for _ in range(R)]
for i, d in enumerate(D):
    Roots[i][i] = 0
    Q = [d]
    Root = [float('inf')] * N
    Root[d] = 0
    while Q and (float('inf') in Roots[i]):
        q = heapq.heappop(Q)
        fatigue, now = divmod(q, 10**3)
        if now in Dest:
            Roots[i][Dtod[now]] = min(fatigue, Roots[i][Dtod[now]])
            Roots[Dtod[now]][i] = min(fatigue, Roots[Dtod[now]][i])
        for nex, cost in Map[now]:
            if Root[nex] > cost + fatigue:
                Root[nex] = cost + fatigue
                heapq.heappush(Q, (cost + fatigue) * 10**3 + nex)

DP = [[float('inf')] * (1 << R) for _ in range(R)]
bit_count = [0]
for _ in range(R):
    bit_count += [x+1 for x in bit_count]

for i in range(1 << R):
    cnt = bit_count[i]
    for j in range(R):
        if (i >> j) & 1 ==1:
            if cnt == 1:
                DP[j][i] = 0
            for k in range(R):
                if j == k:
                    continue
                DP[k][i|(1 << k)] = min(DP[k][i|(1 << k)], DP[j][i] + Roots[j][k])
ans = float('inf')
for i in range(R):
    ans = min(ans, DP[i][-1])
print(ans)

