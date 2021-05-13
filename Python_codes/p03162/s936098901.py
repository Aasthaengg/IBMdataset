def maxExept(lis):
    data = [0,0,0]
    data[0] = max(lis[1],lis[2])
    data[1] = max(lis[0],lis[2])
    data[2] = max(lis[0],lis[1])
    return data
k = int(input())
grid = []
for i in range(k):
  x = list(map(int,input().split(' ')))
  grid.append(x)
for i in range(len(grid)-2,-1,-1):
    x,y,z = maxExept(grid[i+1])
    grid[i][0] +=x
    grid[i][1] +=y
    grid[i][2] +=z
print(max(grid[0]))    