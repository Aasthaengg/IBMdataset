#n = int(input())
import random
import sys
sys.setrecursionlimit(10 ** 7)
n, m = map(int, input().split())
#n=200000
#m=200000
#al = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
adjl = [[] for _ in range(n+1)]
NIL = -1
appear = {}
isalone = {}
for i in range(m):
    a, b = map(int, input().split())
    #a=random.randrange(1,n+1)
    #b=random.randrange(1,n+1)
    #while a==b:
    #    b=random.randrange(1,n+1)
    #print(a,b)
    if appear.get((a, b), False) or appear.get((a, b), False):
        continue
    appear[(a, b)] = True
    appear[(b, a)] = True
    isalone[a] = False
    isalone[b] = False
    adjl[a].append(b)
    adjl[b].append(a)

color = [NIL for i in range(n+1)]
color_id = 0


def dfs(u, color_id):
    global color
    color[u] = color_id
    for v in adjl[u]:
        if color[v] == NIL:  # 未到達なら再起呼び出し
            color[v] = color_id
            dfs(v, color_id)


for u in range(1, n+1):
    if color[u] == NIL:
        color_id += 1
        dfs(u, color_id)

group = {}
for i in range(1, n+1):
    if isalone.get(i, True):
        continue
    group[color[i]] = group.get(color[i], 0)+1

mx = 1
for k, v in group.items():
    mx = max(mx, v)

print(mx)
