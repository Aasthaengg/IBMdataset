path=[list(map(int,input().split())) for _ in range(3)]
city=[1,1,1,1]

for i in range(3):
    city[path[i][0]-1]=city[path[i][0]-1]-1
    city[path[i][1] - 1] = city[path[i][1] - 1] - 1
city.sort()
if (city[1]==-1)and(city[2]==0):
    print("YES")
else:
    print("NO")