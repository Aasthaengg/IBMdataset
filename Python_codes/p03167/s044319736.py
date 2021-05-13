mod = 10**9 + 7
H, W = map(int, input().split())
Maze = [[0]*(W+1) for _ in range(H+1)]
Memo = [[0]*(W+1) for _ in range(H+1)]
Memo[H-1][W-1] = 1
for i in range(H):
    S = input()
    for j in range(W):
        Maze[i][j] = S[j]

for a in range(H-1, -1, -1):
    for b in range(W-1, -1, -1):
        if Maze[a][b] == '#':
            Memo[a][b] = 0
        elif (a == H-1) and (b == W-1):
            continue
        else:
            Memo[a][b] = Memo[a+1][b] + Memo[a][b+1]
            Memo[a][b] %= mod
print(Memo[0][0])
