import math

N,D = map(int,input().split())
xy = [list(map(int,input().split())) for xy in range(N)]
kosuu = 0;
for i in xy:
    if math.sqrt(i[0]**2+i[1]**2) <= D:
        kosuu+=1
print(kosuu)