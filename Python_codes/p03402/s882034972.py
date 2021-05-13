a,b=map(int,input().split())
grid=[['.']*100 for _ in range(100)]

for i in range(50):
    for j in range(100):
        grid[i][j]='#'

nx=0
ny=0
for _ in range(a-1):
    grid[ny][nx]='.'
    if nx<98:
        nx+=2
    else:
        nx=0
        ny+=2

nx=0
ny=51
for _ in range(b-1):
    grid[ny][nx]='#'
    if nx<98:
        nx+=2
    else:
        nx=0
        ny+=2

print(100,100)
for i in range(100):
    print(*grid[i],sep='')