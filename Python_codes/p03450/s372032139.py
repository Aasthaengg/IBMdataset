import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


from collections import defaultdict
n,m = map(int, input().split())
ns = defaultdict(set)
for _ in range(m):
    u,v,c = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].add((c,v))
    ns[v].add((-c,u))
vals = [None] * n
def dijkstra(start):
    h = [start]
    vals[start] = 0
    ans = True
    while h:
        u = h.pop()
        for d, v in ns[u]:
            if vals[v] is None:
                vals[v] = vals[u]+d
                h.append(v)
            else:
                if vals[v]!=vals[u]+d:
                    return False
    return ans

for start in range(n):
    if vals[start] is not None:
        continue
    res = dijkstra(start)
    if not res:
        print("No")
        break
else:
    print("Yes")