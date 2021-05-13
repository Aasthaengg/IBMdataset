import heapq as hq
N = int(input())
L = [set() for _ in range(N)]
for _ in range(N-1):
    u, v, w = list(map(int, input().split()))
    u -= 1
    v -= 1
    L[u].add((w, v))
    L[v].add((w, u))
# print(L)

INF = float('inf')
D = [INF]*N
D[0] = 0
task = []
hq.heapify(task)
for w, v in L[0]:
    hq.heappush(task, (w, v))
while task:
    w, v = hq.heappop(task)
    # print(v,w)
    if D[v] <= w:
        continue
    D[v] = w
    for y, x in L[v]:
        hq.heappush(task, (w+y, x))
# print(D)

for i in range(N):
    print(D[i] % 2)
