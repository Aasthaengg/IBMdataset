MOD = 10 ** 9 + 7
h, w = map(int, input().split())
grid = '#' * (w + 2)
for _ in range(h):
    grid += '#' + input() + '#'
grid += '#' * (w + 2)
D = [0] * len(grid)
start = w + 3
goal = -(w + 4)
D[start] = 1
for i in range(start + 1, len(grid)):
    if grid[i] == '#':
        continue
    D[i] = (D[i - 1] + D[i - (w + 2)]) % MOD
print(D[goal])