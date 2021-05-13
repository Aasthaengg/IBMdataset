import math

def calc_dist(pta, ptb):
    return abs(pta[0] - ptb[0]) + abs(pta[1] - ptb[1])

n, m = map(int, input().split())
stdts = [tuple(map(int, input().split())) for _ in range(n)]
cpts = [tuple(map(int, input().split())) for _ in range(m)]

for stdt in stdts:
    dist_min = math.inf
    for i in range(m):
        dist = calc_dist(stdt, cpts[i])
        if dist < dist_min:
            dist_min = dist
            ans = i + 1
    print(ans)
