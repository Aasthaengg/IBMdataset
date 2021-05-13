import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


from collections import defaultdict
n,U,V = map(int, input().split())
U -= 1
V -= 1
ns = defaultdict(set)
for _ in range(n-1):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].add(v)
    ns[v].add(u)

def bfs(start, ng=None):
    from queue import deque
    q = deque([start])
    seen = [None] * n
    dist = [None] * n
    dist[start] = 0
    seen[start] = -1
    while q:
        u = q.pop()
        d = dist[u]
        for v in ns[u]:
            if seen[v] is None and (ng is None or v!=ng):
                seen[v] = u
                dist[v] = d + 1
                q.appendleft(v)
    return seen, dist
ps, du = bfs(U)
_, dv = bfs(V)
l = []
tmp = V
while tmp!=U:
    l.append(tmp)
    tmp = ps[tmp]
d = len(l)
l = l[::-1]
dist = d//2 if d%2 else d//2-1
ng = l[dist]
start = U if dist==0 else l[dist-1]
_, D = bfs(start, ng=ng)
if max(item for item in D if item is not None)==0:
    ans = dv[start] - 1
else:
    ans = -1
    for i,num in enumerate(D):
        if num is None:
            continue
        val = num + dv[start] - 1#((dv[num]-du[num])%2==1)
        ans = max(ans, val)
print(ans)