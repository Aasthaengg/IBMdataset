N = int(input())
pos = []
for n in range(N):
    x, y = map(int, input().split())
    pos.append((x, y))

import math
from itertools import permutations
list = [i for i in range(N)]
per = permutations(list,N)

ans = 0
for i in per:
    for j in range(N-1):
        x1, y1 = pos[i[j]]
        x2, y2 = pos[i[j+1]]
        ans += math.sqrt((x1-x2)**2 + (y1-y2)**2)
        
for n in range(1,N+1):
    ans /= n

print(ans)