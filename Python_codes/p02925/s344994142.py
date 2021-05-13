from copy import deepcopy
from heapq import heappop, heappush

n = int(input())
a = [list(map(lambda x:int(x) - 1, input().split())) for _ in range(n)]

d = [0] * n

ans = 0
temp = []
for x in range(n):
    heappush(temp, x)
while 1:
    next_temp = []
    while len(temp) > 0:
        x = heappop(temp)
        if d[x] >= n-1:
            continue
        y = a[x][d[x]]
        #print(x, y)
        if y not in next_temp:
            if a[y][d[y]] == x:
                heappush(next_temp, x)
                heappush(next_temp, y)
    #print(next_temp)
    for t in next_temp:
        d[t] += 1
    if len(next_temp) == 0:
        break
    temp = [] + next_temp
    ans += 1

#print(d)

if d.count(n-1) == n:
    print(ans)
else:
    print(-1)
