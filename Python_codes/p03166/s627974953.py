import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


def dfs(start):
    q = [start]
    d0 = 0
    d1 = 0
    while q:
        u = q.pop()
        if u>=0:
            if seen[u]:
                continue
            seen[u] = d0
            d0 += 1
            q.append(~u)
            for v in ns[u]:
                if seen[v] is None:
                    q.append(v)
        else:
            if ns[~u]:
                done[~u] = max(done[v] for v in ns[~u]) + 1
            else:
                done[~u] = 0

n,m = map(int, input().split())
from collections import defaultdict
ns = defaultdict(set)
for i in range(m):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].add(v)

# 行きがけ順
seen = [None] * n
# 帰りがけ順
done = [None] * n
    
for i in range(n):
    if seen[i] is not None:
        continue
    dfs(i)
print(max(done))