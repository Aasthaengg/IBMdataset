import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
XY = []
for _ in range(N):
    x, y = mapint()
    XY.append((x, y))

from collections import defaultdict, Counter
dic = []
for i in range(N):
    x1, y1 = XY[i]
    for j in range(N):
        if i==j:
            continue
        x2, y2 = XY[j]
        dx, dy = x2-x1, y2-y1
        if dx==0 and dy==0:
            continue
        dic.append((dx, dy))
c = Counter(dic)
if len(c)==0:
    print(N)
else:
    (x, y), cnt = c.most_common()[0]
    print(N-cnt)