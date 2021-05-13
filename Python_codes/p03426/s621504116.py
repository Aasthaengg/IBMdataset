H, W, D = map(int, input().split())
grid = []
memo = [[] for _ in range(H*W+1)]
for i in range(H):
    grid.append(list(map(int, input().split())))
    for j in range(len(grid[i])):
        memo[grid[i][j]].append(i)
        memo[grid[i][j]].append(j)

S = [0 for i in range(H*W+1)]

for i in range(H*W+1):
    if(i <= D):
        continue
    S[i] = S[i-D]+ abs(memo[i][0]-memo[i-D][0])+abs(memo[i][1]-memo[i-D][1])

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(S[r]-S[l])