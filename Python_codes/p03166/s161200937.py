import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")



n,m = map(int, input().split())
from collections import defaultdict
ns = defaultdict(set)
for i in range(m):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].add(v)

ds = {}
def sub(u):
    if u in ds:
        return ds[u]
    d = 0
    for v in ns[u]:
        d = max(d, sub(v)+1)
    ds[u] = d
    return d

for i in range(n):
    if i not in ds:
        sub(i)
print(max(ds.values()))