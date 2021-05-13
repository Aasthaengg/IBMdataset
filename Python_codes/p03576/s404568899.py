import sys
from itertools import combinations 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, readline().split())
X = []
Y = []
XY = []
for _ in range(N):
    x,y = map(int,readline().split())
    X.append(x)
    Y.append(y)
    XY.append((x,y))
INF = 10**31
ans = INF
for x1,x2 in combinations(X,2):
    for y1,y2 in combinations(Y,2):
        if x1 > x2:
            x1,x2 = x2,x1
        if y1 > y2:
            y1,y2 = y2,y1
        cnt = 0 
        for x,y in XY:
            if x1 <= x <= x2 and y1 <= y <= y2:
                cnt += 1 
        if cnt >= K:
            tmp = (x2-x1)*(y2-y1)
            ans = min(ans,tmp)

print(ans)