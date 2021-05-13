#エイシング プログラミング コンテスト 2019 -C Alternating Path
"""
s(#に限る),g(.に限る)の座標を任意に定めたとき、
4近傍で#.#.#.と交互に移動できるものの数を求めよ
(但し、s,gが同一でそのような道が複数あっても、1つしかカウントしない)
各#から何回.を通れるかをdfsで求めれば良い。
ちなみに、その時に#を通れば、その#は今dfsを行っている#と同じだけの組み合わせ
を持つので、端折って良い。
"""
import sys
from collections import deque
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
H,W = map(int,readline().split())
maze = []
for _ in range(H):
    maze += [list(readline().rstrip().decode())]
used = [[0]*W for _ in range(H)]
def dfs(y,x):
    white = 0
    black = 1
    deq = deque([(y,x)])
    used[y][x] = 1
    while deq:
        fr = deq.pop()
        for go in [(0,1),(1,0),(0,-1),(-1,0)]:
            if 0 <= fr[0]+go[0] < H and 0 <= fr[1]+go[1] < W:
                if not used[fr[0]+go[0]][fr[1]+go[1]]:
                    if maze[fr[0]][fr[1]] != maze[fr[0]+go[0]][fr[1]+go[1]]:
                        deq.append((fr[0]+go[0],fr[1]+go[1]))
                        used[fr[0]+go[0]][fr[1]+go[1]] = 1
                        if maze[fr[0]+go[0]][fr[1]+go[1]] == ".":
                            white += 1
                        else:
                            black += 1
    
    return white * black
ans = 0
for i in range(H):
    for j in range(W):
        if not used[i][j] and maze[i][j] == "#":
            ans += dfs(i,j)

print(ans)