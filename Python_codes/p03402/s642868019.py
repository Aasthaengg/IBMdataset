a, b = map(int, input().split())
n = 24
unit = [
    '####',
    '#.#.',
    '#.#.',
    '....'
]
row = [
    '.' + unit[0]*n + '#',
    '.' + unit[1]*n + '#',
    '.' + unit[2]*n + '#',
    '.' + unit[3]*n + '#'
]
grid = []
for i in range(n):
    grid.append(list(row[0]))
    grid.append(list(row[1]))
    grid.append(list(row[2]))
    grid.append(list(row[3]))
"""
# 黒
for i in range(n):
    grid[0][4*(i+1)] = 'x'
for i in range(n):
    grid[4*i][4] = 'y'
# 白
for i in range(n):
    grid[2][4*(i+1)-2] = 'w'
for i in range(n):
    grid[4*(i+1)-2][2] = 'v'
"""
# 白
for i in range(a//n+1):
    for j in range(n):
        if i * n + j < a-1:
            #print('#',4*(j+1)-2,4*(i+1)-2)
            grid[4*(i+1)-2][4*(j+1)-2] = '#'

# 黒
for i in range(b//n+1):
    for j in range(n):
        if i * n + j < b-1:
            #print('.',4*j,4*(i+1))
            grid[4*i][4*(j+1)] = '.'

print(len(grid), len(grid[0]))
for i in grid:
    print(''.join(i))

