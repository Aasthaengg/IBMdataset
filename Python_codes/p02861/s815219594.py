import itertools
import math

n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

root = {}
for i in range(n-1):
    ix, iy = xy[i][0], xy[i][1]
    for j in range(i+1, n):
        jx, jy = xy[j][0], xy[j][1]
        root[(i, j)] = ((ix-jx)**2+(iy-jy)**2)**(1/2)

long = 0
for i in itertools.permutations([i for i in range(n)]):
    for j in range(1, len(i)):
        long += root[tuple(sorted([i[j-1], i[j]]))]
print(long/math.factorial(n))
