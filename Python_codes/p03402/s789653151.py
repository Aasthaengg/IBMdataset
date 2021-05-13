a,b = map(int, input().split())
w = 100
h = 20
grid = []
for _ in range(h):#黒
    grid.append(['#' for i in range(w)])
for _ in range(h):#白
    grid.append(['.' for i in range(w)])
n = 0
for i in range(0,a-1):
    if i % 50 == 0 and i != 0:
        n += 2
    grid[n][2*(i % 50)] = '.'

n = h+1
for i in range(0,b-1):
    if i % 50 == 0 and i != 0:
        n += 2
    grid[n][2*(i % 50)] = '#'

print(2*h,w)
for i in range(2*h):
    print(''.join(grid[i]))
