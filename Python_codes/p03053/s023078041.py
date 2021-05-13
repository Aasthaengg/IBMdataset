#AGC033-A Darker and Darker
"""
愚直にbfs(queueが無くなるまで)
"""
import sys
from collections import deque
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

#迷路plane
H,W = map(int,readline().split())
maze = []
for _ in range(H):
    maze += [list(readline().rstrip().decode())]

def bfs(lst):
    deq = deque(lst)
    ans = 0
    while deq:
        h,w,now = deq.popleft()
        for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
            if not (0 <= h+a < H and 0 <= w+b < W):continue
            if maze[h+a][w+b]=="#":continue
            else:
                maze[h+a][w+b] = "#"
                ans = max(ans,now+1)
                deq.append([h+a,w+b,now+1])
    return ans

lst1 = []
for i in range(H):
    for j in range(W):
        if maze[i][j] == "#":
            lst1.append([i,j,0])

print(bfs(lst1))