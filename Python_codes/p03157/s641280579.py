from collections import deque,defaultdict
import sys
from collections import defaultdict
input = sys.stdin.readline

H, W = map(int, input().split())
C = [list(input()) for i in range(H)]
INF = 10 ** 9
go = [[1, 0], [0, 1], [-1, 0], [0, -1]]
que = deque()
ans  = -1

mass = ["#","."]
groups = [[-1 for _ in range(W)] for _ in range(H)]
group_num = -1
for sx in range(W):
    for sy in range(H): # スタート地点のループ
        if C[sy][sx] == "#" and groups[sy][sx] == -1:
            group_num += 1
            que.append((sy,sx))
            groups[sy][sx] = group_num
            while que: #行けるだけいく
                y,x = que.popleft()
                for temp in go:
                    gx,gy = temp
                    nx = x + gx
                    ny = y + gy
                    should = abs(sx - nx) + abs(sy - ny) #奇数→
                    should %= 2
                    if 0<= nx < W and 0<= ny < H and C[ny][nx] == mass[should]:
                        if groups[ny][nx] == -1: # ここの更新にminはいらない(幅優先なので自明に最短距離を進む)
                            groups[ny][nx] = group_num
                            que.append( (ny,nx))
ans = 0
di_sharp = defaultdict(lambda :0)
di_dot = defaultdict(lambda :0)
ma = -1
for sx in range(W):
    for sy in range(H):
        if groups[sy][sx] >= 0:
           color = groups[sy][sx]
           ma = max(ma,color)
           if C[sy][sx] =="#":
               di_sharp[color] += 1
           else:
               di_dot[color] += 1

for i in range(ma + 1):
    ans += di_dot[i]  * di_sharp[i]

print(ans)



