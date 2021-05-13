import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m,p = map(int, input().split())
ns = [[] for _ in range(n)]
rns = [[] for _ in range(n)]

mc = -1
for _ in range(m):
    u,v,c = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].append((p-c,v))
    rns[v].append(u)
q = [n-1]
seen = [False]*n
seen[n-1] = True
while q:
    u = q.pop()
    for v in rns[u]:
        if seen[v]:
            continue
        seen[v] = True
        q.append(v)
def bf(start):
    dist = [float("inf")]*n
    dist[start] = 0
    for i in range(n):
        for u in range(n):
            if dist[u]==float("inf"):
                continue
            for c,v in ns[u]:
                if dist[v] > dist[u] + c:
                    dist[v] = dist[u] + c
                    if i>=n-1 and seen[v]:
                        return -1
    return dist

dist = bf(0)
if dist==-1:
    ans = -1
else:
    ans = max(0, dist[n-1]*-1)
print(ans)