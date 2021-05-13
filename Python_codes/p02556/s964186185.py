n = int(input())

points = []

for i in range(n) :
    point = list(map(int, input().split(" ")))
    points.append(point)

z = []
w = []

for i in range(len(points)) :
    z.append(points[i][0] + points[i][1])

for i in range(len(points)) :
    w.append(points[i][0] - points[i][1])

max_z = max(z) - min(z)
max_w = max(w) - min(w)

if max_z > max_w :
    print(max_z)
else :
    print(max_w)
