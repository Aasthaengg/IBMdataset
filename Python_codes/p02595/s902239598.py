import math

n, d = (int(a) for a in input().split())
list_xy = [[int(x) for x in input().split()] for y in range(0, n)]
count = 0

for i in range(0, n):
    dist = math.sqrt(list_xy[i][0] ** 2 + list_xy[i][1] ** 2)
    if dist <= d:
        count += 1

print(count)