H,W = [int(i) for i in input().split()]

maze = [['.']*(W+2)]
for i in range(H):
    maze.append(list('.'+input()+'.'))
maze.append(['.']*(W+2))

ans = [[0]*W for _ in range(H)]
for i in range(1,H+1):
    for j in range(1,W+1):
        if maze[i][j] == '#':
            ans[i-1][j-1] = '#'
        else:
            for p,q in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]:
                if maze[i+p][j+q] == '#':
                    ans[i-1][j-1] += 1

for i in range(H):
    for j in range(W):
        print(ans[i][j],end='')
    print()
