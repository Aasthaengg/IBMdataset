x, y = map(int, input().split())
grid = []
visit = []
mod = 1000000007
for _ in range(x):
    grid.append([i for i in input()])
    visit.append([0 for i in range(y)])
grid[x-1][y-1] = 'X'
visit[x-1][y-1] = 1
for i in range(x-1, -1, -1):
    for j in range(y-1, -1, -1):
        if grid[i][j] == '.':
            if i < x-1 and j < y-1:
                visit[i][j] = (visit[i][j+1] + visit[i+1][j])%mod
            elif i < x-1 and j == y-1:
                visit[i][j] = visit[i+1][j]
            else:
                visit[i][j] = visit[i][j+1]
print(visit[0][0])
        
            
