import sys
from collections import deque



readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prl = lambda x: print(*x ,sep='\n')

def bfs(start):
    tansaku = deque(start)
    visited = {i:set() for i in range(h)}
    res = 0
    black = len(start)
    while black != h*w:
        for _ in range(len(tansaku)):
            pre_y,pre_x = tansaku.popleft()
            if pre_x in visited[pre_y]:
                continue
            for i in range(pre_x-1,pre_x+2,2):
                if 0 <= i <= w-1 and tizu[pre_y][i] == '.':
                    tansaku.append([pre_y,i])
                    tizu[pre_y][i] = '#'
            for j in range(pre_y-1,pre_y+2,2):
                if 0 <= j <= h-1 and tizu[j][pre_x] == '.':
                    tansaku.append([j,pre_x])
                    tizu[j][pre_x] = '#'
            visited[pre_y].add(pre_x)
        black += len(tansaku)
        res += 1
    return res

h,w = nm()
tizu = []
sharp = []
for i in range(h):
    temp = list(input())
    s_temp = [[i,j] for j in range(w)  if temp[j] == '#' ]
    tizu.append(temp)
    sharp += s_temp
ans = bfs(sharp)
print(ans)