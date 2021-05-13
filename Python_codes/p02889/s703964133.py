import sys
input = lambda: sys.stdin.readline().rstrip()
inpl = lambda: list(map(int,input().split()))
def warshall_floyd(N, edges,
                   nopath=None,
                   start_distance=0,
                   plus_func=lambda D,d: D+d):
    '''
    edges: list of set
        edges = [{(y0, distance0), (y1, distance1), ...}, ...]
    '''
    ret = [[nopath]*N for _ in range(N)]
    for i in range(N):
        ret[i][i] = start_distance
    for i in range(N):
        for j, d in edges[i]:
            if 0 <= j < N:
                ret[i][j] = plus_func(start_distance, d)
    for k in range(N):
        for i in range(N):
            if i == k: continue
            for j in range(N):
                if j == k or ret[i][k] == nopath or ret[k][j] == nopath:
                    continue
                d = plus_func(ret[i][k], ret[k][j])
                if ret[i][j] == nopath or d < ret[i][j]:
                    ret[i][j] = d
    return ret

N, M, L = inpl()
road = [[] for _ in range(N)]
for i in range(M):
    A, B, C = inpl()
    if C <= L:
        road[A-1].append((B-1,C))
        road[B-1].append((A-1,C))

Q = int(input())
ST = []
goals = [set() for _ in range(N)]
for _ in range(Q):
    s, t = inpl()
    s -= 1
    t -= 1
    ST.append((s, t))

distance = warshall_floyd(N, road)
path = [set() for _ in range(N)]
for i in range(N):
    for j in range(N):
        d = distance[i][j]
        if d is not None and d <= L:
            path[i].add((j,1))
ans = warshall_floyd(N, path)
for s, t in ST:
    if ans[s][t] is None:
        print(-1)
    else:
        print(ans[s][t]-1)
