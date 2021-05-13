
N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]

ans = 0

def measure(originX,originY):
    dist = []
    for X,Y in XY:
        dist.append(abs(X-originX)+abs(Y-originY))
    return max(dist)-min(dist)

originX = 0
originY = 0
ans = max(ans,measure(originX,originY))

originX = 10**9
originY = 0
ans = max(ans,measure(originX,originY))

originX = 0
originY = 10**9
ans = max(ans,measure(originX,originY))

originX = 10**9
originY = 10**9
ans = max(ans,measure(originX,originY))

print(ans)