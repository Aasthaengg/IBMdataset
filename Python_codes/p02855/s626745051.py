#template
from collections import Counter
def inputlist(): return [int(i) for i in input().split()]
#template
H,W,K = inputlist()
cake = ['0']*H
for i in range(H):
    cake[i] = list(input())
seen = [[False]*W for _ in range(H)]
ans = [[0]*W for _ in range(H)]
indexa = 1
for x in range(H):
    for y in range(W):
        if cake[x][y] == '#':
            ans[x][y] = indexa
            indexa +=1
for x in range(H):
    for y in range(1,W):
        if ans[x][y-1] != 0:
            if ans[x][y] == 0:
                ans[x][y] = ans[x][y-1]
for x in range(H):
    for j in range(1,W):
        y = (W-1)-j
        if ans[x][y+1] != 0:
            if ans[x][y] == 0:
                ans[x][y] = ans[x][y+1]
for x in range(1,H):
    for y in range(W):
        if ans[x-1][y] != 0:
            if ans[x][y] == 0:
                ans[x][y] = ans[x-1][y]
for i in range(1,H):
    x = (H-1)-i
    for y in range(W):
        if ans[x+1][y] != 0:
            if ans[x][y] == 0:
                ans[x][y] = ans[x+1][y]
for i in range(H):
    print(*ans[i])