from collections import deque

INF = float('inf')

H, W = map(int, input().split())
Sss = ['#'*(W+2)] + ['#'+input()+'#' for _ in range(H)] + ['#'*(W+2)]

def bfsGridGraph(Sss, xS, yS, INF):
    dxys = [(-1,0), (1,0), (0,-1), (0,1)]
    distss = [[(INF if S != '#' else -1) for S in Ss] for Ss in Sss]
    distss[xS][yS] = 0
    Q = deque([(xS, yS)])
    while Q:
        x, y = Q.popleft()
        dist = distss[x][y]
        for dx, dy in dxys:
            x2, y2 = x+dx, y+dy
            if distss[x2][y2] == INF:
                distss[x2][y2] = dist + 1
                Q.append((x2, y2))
    return distss

ans = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        if Sss[i][j] == '#': continue
        distss = bfsGridGraph(Sss, i, j, INF)
        maxDist = max(map(max, distss))
        ans = max(ans, maxDist)

print(ans)
