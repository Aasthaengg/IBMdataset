H,W = map(int,input().split())
H += 2; W += 2
grid = '#' * W
for _ in range(H-2):
    grid += '#' + input() + '#'
grid += '#' * W

for i in range(H):
    print(grid[i*W:(i+1)*W])