n,m = list(map(int,input().strip().split()))

grid = []
for i in range(m):
  array = list(map(int, input().strip().split()))
  grid.append(array)
  
for i in range(1,n+1):
  road = 0
  for j in grid:
    if i in j:
      road +=1
  print(road)