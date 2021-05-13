n = int(input())
 
difs = {}
points = []
 
for i in range(n):
    x, y = list(map(int, input().split()))
 
    for j in range(len(points)):
        dif1 = (points[j][0] - x, points[j][1] - y)
        dif2 = (-dif1[0], -dif1[1])
 
        difs[dif1] = 1 if dif1 not in difs else difs[dif1] + 1
        difs[dif2] = 1 if dif2 not in difs else difs[dif2] + 1
 
    points.append((x, y))
 
if n == 1:
    print(1)
else:
    print(n-max(difs.values()))