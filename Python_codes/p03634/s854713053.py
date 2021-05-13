import sys
sys.setrecursionlimit(10**8)

N = int(input())

vertex = [{} for _ in range(N)]

for i in range(N-1):
    a,b,c = map(int,input().split())
    vertex[a-1][b-1] = c
    vertex[b-1][a-1] = c

Q,K = map(int,input().split())

d = [0 for i in range(N)]

def dfs(v1,v2):
    d[v2] = d[v1] + vertex[v1][v2]
    for v in vertex[v2]:
        if v == v1:
            continue
        dfs(v2,v)

for v in vertex[K-1].keys():
    dfs(K-1,v)

for q in range(Q):
    x,y = map(int,input().split())
    print(d[x-1] + d[y-1])
