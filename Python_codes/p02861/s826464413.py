n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]

import math
dist = 0
for i in range(n):
    for j in range(n):
        dist += math.sqrt((xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2)

print(dist/n)
