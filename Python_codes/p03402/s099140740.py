A,B = map(int,input().split())
grid = [['#' for j in range(100)] for i in range(50)] + [['.' for j in range(100)] for i in range(50)]

for i in range(A-1):
    q,r = divmod(i,50)
    grid[q*2][r*2] = '.'
    
for i in range(B-1):
    q,r = divmod(i,50)
    grid[-1-q*2][-1-r*2] = '#'
    
print(100,100)

for g in grid:
    print(''.join(g))