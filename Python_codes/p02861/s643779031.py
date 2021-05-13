import math
N = int(input())
xy = []
length = 0
for i in range(N):
    x, y = map(int, input().split())
    if i!=0:
        for j in xy:
            length+=math.sqrt((x-j[0])**2+(y-j[1])**2)
    
    
    xy.append([x, y])
    
            
print(length*2/N)