from operator import itemgetter

N = int(input())
xyhs = [list(map(int, input().split())) for _ in range(N)]

xyhs.sort(key=itemgetter(2), reverse=True)

lsts = []

xyh = xyhs[0]
for cy in range(101):
    for cx in range(101):
        lsts.append([cx, cy, xyh[2] + abs(xyh[0] - cx) + abs(xyh[1] - cy)]) 

for xyh in xyhs[1:]:
    lst = []
    while len(lsts):      
        p = lsts.pop()
        h = xyh[2] + abs(xyh[0] - p[0]) + abs(xyh[1] - p[1])
        if p[2] == h:
            lst.append(p)
    lsts = lst[:]
    if len(lsts) == 1: break
print(*lsts[0])
