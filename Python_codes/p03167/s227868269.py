import sys
 
sys.setrecursionlimit(100000)
 
H, W = map(int, input().split())

stage = []
for h in range(H):
    a = list(input())
    stage.append(a)

memo = [[-1 for i in range(W)] for j in range(H)]

def move(x, y):
    if x >= W or y>=  H:
        return 0
    if x == W-1 and y == H-1:
        return 1
    if stage[y][x] == "#":
        return 0
    if memo[y][x] != -1:
        return memo[y][x]
    p = move(x+1, y)+move(x,y+1)
    memo[y][x] = p
    return p

print(move(0,0)%(10**9+7))