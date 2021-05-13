import sys
sys.setrecursionlimit(100000)
N = int(input())
ab = [list(map(int, input().split())) for _ in range(N-1)]
c = list(map(int, input().split()))

if N == 1:
    print(0)
    print(c[0])
    exit()

c.sort(reverse = True)
edge = [[] for _ in range(N)]
for a, b in ab:
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

def dfs(v, p):
    global ans
    global count
    if p != -1:
        anse[v] = c[count+1]
        ans += min(anse[v], anse[p])
        count += 1
    for nv in edge[v]:
        if nv == p:
            continue
        dfs(nv, v)

#search = [i for i, e in enumerate(edge) if len(e) == 1]
search = [0]
res = 0
rese = [None for _ in range(N)]
for i in search:
    count = 0
    ans = 0
    anse = [None for _ in range(N)]
    anse[i] = c[0]
    dfs(i, -1)
    if res < ans:
        res = ans
        rese = anse
print(res)
print(" ".join(map(str, rese)))