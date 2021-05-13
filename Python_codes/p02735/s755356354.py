inputs = [s.strip() for s in open(0).readlines()]
import numpy as np
class Grid():
    def __init__(self, grid, w=0, h=0, function=lambda x: x):
        self.w = w = w if w else len(grid[0])
        self.h = h = h if h else len(grid)
        dtype = type(function(grid[0][0]))
        self.grid = np.empty((h, w), dtype=dtype)
        for i, row in zip(range(h), grid):
            for j, val in zip(range(w), row):
                self.grid[i][j] = function(val)
    
    def is_valid_x(self, x):
        return 0 <= x < self.w
    def is_valid_y(self, y):
        return 0 <= y < self.h
    def is_valid_xy(self, x, y):
        return self.is_valid_x(x) and self.is_valid_y(y) 
    
    def __iter__(self):
        return iter(self.grid)
    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])
    def __getitem__(self, x):
        return self.grid[x]
    def __setitem__(self, x, val):
        self.grid[x] = val

h, w = map(int, inputs[0].split())
grid = Grid(inputs[1:]).grid

h, w = map(int, inputs[0].split())
grid = Grid(inputs[1:])

dp = Grid(np.zeros((h, w), np.int))
dp[0, 0] = int(grid[0, 0] == '#')
for i in range(1, w):
    dp[0, i] = dp[0, i-1] + int(grid[0, i-1] + grid[0, i] == '.#')
for i in range(1, h):
    dp[i, 0] = dp[i-1, 0] + int(grid[i-1, 0] + grid[i, 0] == '.#')
x = y = 1
while not (x == w-1 and y == h-1):
    for i in range(x, w):
        dp[y, i] = min(dp[y, i-1] + int(grid[y, i-1] + grid[y, i] == '.#'),
                       dp[y-1, i] + int(grid[y-1, i] + grid[y, i] == '.#'))
    for i in range(y+1, h):
        dp[i, x] = min(dp[i-1, x] + int(grid[i-1, x] + grid[i, x] == '.#'),
                       dp[i, x-1] + int(grid[i, x-1] + grid[i, x] == '.#'))
    x, y = min(x+1, w-1), min(y+1, h-1)
print(min(dp[y-1, x] + int(grid[y-1, x] + grid[y, x] == '.#'), 
          dp[y, x-1] + int(grid[y, x-1] + grid[y, x] == '.#')))