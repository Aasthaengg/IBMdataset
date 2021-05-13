import itertools
grid = []
for _ in range(3):
    grid.append(list(map(int,input().split())))

sum = sum(list(itertools.chain.from_iterable(grid)))
if sum % 3 != 0:
    print('No')
    exit()

for i in range(-100,101):
    a1 = i
    b1 = grid[0][0] - a1
    b2 = grid[0][1] - a1
    b3 = grid[0][2] - a1
    a2 = grid[1][0] - b1
    a3 = grid[2][0] - b1
    if a1 + a2 + a3 + b1 + b2 + b3 == sum // 3:
        print('Yes')
        exit()
print('No')