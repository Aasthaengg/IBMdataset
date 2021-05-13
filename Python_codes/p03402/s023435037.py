from __future__ import print_function

a, b = map(int, raw_input().split())

h = 101
w = 101

grid = [['.' for i in xrange(w)] for j in xrange(h)]

for i in xrange(51, h):
    for j in xrange(1, w):
        grid[i][j] = '#'

cnt = a - 1 # paint white

for i in xrange(52, h, 2):
    for j in xrange(1, w, 2):
        if cnt == 0: break
        grid[i][j] = '.'
        cnt -= 1
        
    if cnt == 0: break

cnt = b - 1 # paint black

for i in xrange(1, h, 2):
    for j in xrange(1, w, 2):
        if cnt == 0: break
        grid[i][j] = '#'
        cnt -= 1
        
    if cnt == 0: break

print(100, 100)
for i in xrange(1, h):
    for j in xrange(1, w):
        print(grid[i][j], end = "")
    print()
