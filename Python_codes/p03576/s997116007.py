from itertools import combinations

n,k = map(int,input().split())
Px = sorted([list(map(int,input().split())) for i in range(n)])
Py = sorted(Px,key=lambda p:p[1])

area = float('inf')

for x1 in range(n-1):
    for x2 in range(x1+1,n):
        for y1 in range(n-1):

            point = 0
            for y in range(y1,n):
                if Px[x1][0]<=Py[y][0]<=Px[x2][0]:
                    point += 1
                    if point == k:
                        area = min(area,(Px[x2][0]-Px[x1][0])*(Py[y][1]-Py[y1][1]))
                        break

print(area)