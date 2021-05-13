H,W = map(int, input().split())
from sys import stdin
field = []
bque = []
for i in range(H):
    st = stdin.readline()[:-1]
    ls = []
    for j,ss in enumerate(st):
        ls.append(ss)
        if ss=='#':
            bque.append([i,j])

    field.append(ls)

from collections import deque

que = deque([])
que.append(bque)
count = 0
while len(que)>0:
    ll = que.popleft()
    nls = []
    for item in ll:
        x = item[0]
        y = item[1]
        for dx in [-1,1]:
            for dy in [-1,1]:
                if 0<=x+dx<=H-1:
                    if field[x+dx][y]=='.':
                        field[x+dx][y]='#'
                        nls.append([x+dx,y])
                if 0<=y+dy<=W-1:
                    if field[x][y+dy]=='.':
                        field[x][y+dy]='#'
                        nls.append([x,y+dy])
    if len(nls) != 0:
        que.append(nls)
        count += 1
print(count)
"""微妙に遅かった60msぐらい　"""
