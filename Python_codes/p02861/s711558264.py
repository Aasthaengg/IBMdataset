import math
N = int(input())
x = [list(map(int,input().split())) for i in range(N)]

l = []
for i in range(N):
    for j in range(N):
        l.append(math.sqrt((x[i][0]-x[j][0])**2+(x[i][1]-x[j][1])**2))

print(sum(l)/N)