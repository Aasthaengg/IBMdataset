import math

n = int(input())

bi_factors = []

for i in range(1,int(math.sqrt(n)+1)):
    if n%i == 0:
        temp = (i,n//i)
        bi_factors.append(temp)

inf = float('INF')
ans = inf

for point in bi_factors:
    d = point[0] + point[1] - 2
    if ans > d:
        ans = d

print(ans)

