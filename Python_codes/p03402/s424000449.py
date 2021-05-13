A,B = map(int,input().split())
grid = [["." for i in range(0,100)] for j in range(0,100)]
for j in range(50,100):
    for i in range(0,100):
        grid[j][i] = "#"
for count in range(0,B-1):
    x = (count*2)%100
    y = ((count*2)//100)*2
    grid[y][x] = "#"
for count in range(0,A-1):
    x = (count*2)%100
    y = ((count*2)//100)*2
    grid[y+51][x] = "."
print("100 100")
for j in range(0,100):
    for i in range(0,100):
        if i != 99:
            print(grid[j][i],end ="")
        else:
            print(grid[j][i])
