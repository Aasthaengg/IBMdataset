n = int(input())

grid = []
ans = []

for i in range(2):
    grid.append(list(map(int, input().split())))

for i in range(n):
    anst = 0
    for _ in range(n):
        anst = sum(grid[0][:i+1])
        anst += sum(grid[1][i:n])
    ans.append(anst)

print(max(ans))
