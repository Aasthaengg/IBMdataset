H,W,D = list(map(int,input().split()))
grid = [list(map(int,input().split())) for i in range(H)]

num_point = {}
for i in range(H):
    for j in range(W):
        num_point[grid[i][j]] = (i+1,j+1)

Q = int(input())
lst = [0]*(H*W+1)
LR = []
for _ in range(Q):
    LR.append(list(map(int,input().split())))
    lst[LR[-1][0]] += 1
    lst[LR[-1][1]] -= 1

ans_lst = [0]*(H*W+1)

for i in range(1,D+1):
    for j in range(i+D,H*W+1,D):
        sx,sy = num_point[j-D]
        tx,ty = num_point[j]
        ans_lst[j] += ans_lst[j-D]+(abs(tx-sx)+abs(ty-sy))
for L,R in LR:
    print(ans_lst[R]-ans_lst[L])