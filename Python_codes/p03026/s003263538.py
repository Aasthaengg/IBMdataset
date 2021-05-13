import collections, heapq, sys

n = int(sys.stdin.readline().rstrip())
g = collections.defaultdict(list)
visited = set()
deg = collections.defaultdict(int)
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    deg[a] += 1
    deg[b] += 1
    g[a].append(b)
    g[b].append(a)

pq = []
for i in range(1, n+1):
    heapq.heappush(pq, [deg[i], i])
wts = map(int, sys.stdin.readline().rstrip().split(' '))
wts.sort(reverse=True)
    
vToWt = [-1 for _ in range(n+1)]
sm = 0
while len(pq):
    _, v = heapq.heappop(pq)
    
    if vToWt[v] != -1:
        continue
    vToWt[v] = wts.pop()
    for nei in g[v]:
        if vToWt[nei] != -1:
            continue
        sm += vToWt[v]
        deg[nei] -= 1
        heapq.heappush(pq, [deg[nei], nei])

print(sm)
print(' '.join(map(str, [x for x in vToWt[1:]])))


