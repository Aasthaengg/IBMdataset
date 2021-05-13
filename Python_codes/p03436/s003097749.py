import sys
from collections import deque

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prl = lambda x: print(*x ,sep='\n')

def bfs(start,end):
    tansaku = deque()
    tansaku.append(start)
    visited = {i:set() for i in range(h)}
    kyori = [[0]*w for _ in range(h)]
    while tansaku:
        pre_y,pre_x = tansaku.popleft()
        if pre_x in visited[pre_y]:
            continue
        for i in range(pre_x-1,pre_x+2,2):
            if 0 <= i <= w-1 and tizu[pre_y][i] == '.':
                tansaku.append([pre_y,i])
                kyori[pre_y][i] = kyori[pre_y][pre_x] + 1
        for j in range(pre_y-1,pre_y+2,2):
            if 0 <= j <= h-1 and tizu[j][pre_x] == '.':
                tansaku.append([j,pre_x])
                kyori[j][pre_x] = kyori[pre_y][pre_x] + 1
        visited[pre_y].add(pre_x)
        if [pre_y,pre_x] == end:
            return kyori[pre_y][pre_x]
    return -1



h,w = nm()
white = 0
tizu = []
for i in range(h):
    temp = list(input())
    white += temp.count('.')
    tizu.append(temp)
res = bfs([0,0],[h-1,w-1])
if res == -1:
    print(res)
else:
    print(white-(res+1))