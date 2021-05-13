H,W,K = map(int,input().split())
grid = [input() for _ in range(H)]
N = H+W
ans = 0
start = 0
for i in grid:
    start += i.count('#')

for i in range(2**N):
    tmp = start
    painted = []
    for j in range(H):
        if (i>>j)&1:
            tmp -= grid[j].count('#')
            painted.append(j)
    for j in range(W):
        if (i>>j+H)&1:
            for k in range(H):
                if '#' == grid[k][j]:
                    if k in painted:
                        continue
                    else:
                        tmp -= 1
    if tmp == K:
        ans += 1
print(ans)