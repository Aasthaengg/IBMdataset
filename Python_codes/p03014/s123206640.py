def make_mat(grid, H, W):
    res = [[0] * W for _ in range(H)]
    for h in range(H):
        cnt = 0
        for w in range(W):
            if grid[h][w] == 1:
                for i in range(cnt):
                    res[h][w - 1 - i] = cnt
                cnt = 0
            else:
                cnt += 1
        if grid[h][w] == 0:
            for i in range(cnt):
                res[h][w - i] = cnt
    return res

def max2(x,y):
    return x if x > y else y


import sys
input = sys.stdin.readline

H, W = map(int, input().split())


grid = []
grid_t = [[] for _ in range(W)]
for h in range(H):
    temp = []
    for w, s in enumerate(input().rstrip()):
        if s=="#":
            temp.append(1)
            grid_t[w].append(1)
        else:
            temp.append(0)
            grid_t[w].append(0)
    grid.append(temp)

A = make_mat(grid, H, W)
B = make_mat(grid_t, W, H)

res = 0
for h in range(H):
    for w in range(W):
        res = max2(A[h][w] + B[w][h], res)

print(res-1)