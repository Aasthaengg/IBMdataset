from itertools import combinations
from collections import Counter

N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

if N != 1:
    delta = []
    for i, j in combinations(list(range(N)), 2):
        if xy[i][0] < xy[j][0]:
            p0 = xy[i][:]
            p1 = xy[j][:]
        else:
            p0 = xy[j][:]
            p1 = xy[i][:]
        delta.append((p1[0] - p0[0], p1[1] - p0[1]))
    cnt = Counter(delta)
    dlt = cnt.most_common()
    
def calc(dd):
    visited =set()
    c = 0
    for i in range(N):
        if xy[i] in visited:continue
        c += 1
        temp = [[xy[i], c]]
        while temp:
            q = temp.pop()
            for n in [1, -1]:
                x1, y1 = q[0][0] + n * dd[0], q[0][1] + n * dd[1]
                if not (x1, y1) in visited and (x1, y1) in xy:
                    temp.append([(x1, y1), q[1]])
                    visited.add((x1, y1))
    return c

if N == 1: print(1)
else:
    ans = []
    pre = dlt[0][1]
    for lst in dlt:
        ans.append(calc(lst[0]))
    print(min(ans))