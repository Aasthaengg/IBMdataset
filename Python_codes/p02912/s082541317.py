import sys
input = sys.stdin.buffer.readline
from math import log

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

table = [[0]*(int(log(a[-1],2))+2) for i in range(n)]

for i in range(n):
    for y in range(int(log(a[-1],2))+2):
        table[i][y] = a[i]//pow(2,y)
        if a[i]//pow(2,y) == 0:
            break

s_table = [[0]*(int(log(a[-1],2))+2) for i in range(n)]
for i in range(n):
    s_table[i][0] = table[i][0]

import heapq
hq = []
heapq.heapify(hq)
h_push = heapq.heappush
h_pop = heapq.heappop

for i in range(n):
    for y in range(1,int(log(a[-1],2))+2):
        s_table[i][y] = table[i][y]-table[i][y-1]
        h_push(hq,table[i][y]-table[i][y-1])
        if table[i][y]-table[i][y-1] == -1:
            break


ans = sum(a)

for i in range(m):
    if not hq:
        print(0)
        exit()
    ans += h_pop(hq)
    
print(ans)


