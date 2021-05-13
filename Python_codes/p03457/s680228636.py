N = int(input().strip())
gridi = []
for i in range(N):
    array = list(map(int, input().strip().split()))
    gridi.append(array)
f="Yes"
grid=[]
for i in range(N+1):
    grid.append([0,0,0])
for i in range(1,N+1):
    grid[i][0]=gridi[i-1][0]
    grid[i][1]=gridi[i-1][1]
    grid[i][2]=gridi[i-1][2]
for i in range(N):
    dt=int(grid[i+1][0])-int(grid[i][0])
    dist=abs(grid[i+1][1]-grid[i][1])+abs(grid[i+1][2]-grid[i][2])
    if dist>dt:
        f="No"
    elif dist%2!=dt%2:
        f="No"
print(f)