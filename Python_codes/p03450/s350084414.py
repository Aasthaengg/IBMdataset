n,m=map(int,input().split())
g = [[ ] for _ in range(n)]
for _ in range(m):
    l,r,d = map(int,input().split())
    g[l-1].append((d,r-1))
    g[r-1].append((-d,l-1))
inf = 12345678901234
dist = [inf]*n

import queue
q=queue.Queue()
for i in range(n):
    if dist[i] != inf: continue
    dist[i] = 0
    q.put((0,i))
    while not q.empty():
        cost, nown = q.get()
        for nextc, nextn in g[nown]:
            if dist[nextn] != inf:
                if dist[nextn] != cost + nextc:
                    print('No')
                    exit()
            else:
                dist[nextn] = cost+nextc
                q.put((dist[nextn], nextn))
print('Yes')
