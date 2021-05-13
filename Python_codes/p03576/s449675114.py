import itertools
import math


LIM = 50
N,K = list(map(int,input().split(" ")))

Xs = []
Ys = []

dots = []
for _ in range(N):
    x,y = (map(int,input().split(" ")))
    Xs.append(x)
    Ys.append(y)
    dots.append((x,y))

Xs.sort()
Ys.sort()

ans = -1
for x1 in range(N):
    for x2 in range(x1 + 1,N):
        for y1 in range(N):
            for y2 in range(y1 + 1,N):
                cot = 0
                underX = Xs[x1]
                upperX = Xs[x2]
                underY = Ys[y1]
                upperY = Ys[y2]

                for k in range(N):
                    if   underX<= dots[k][0] <= upperX and underY <= dots[k][1] <= upperY:
                        cot += 1
                if cot >= K:
                    S = (upperX - underX) * (upperY - underY)
                    if ans == -1:
                        ans = S
                    ans = min( ans ,S)
print(ans)