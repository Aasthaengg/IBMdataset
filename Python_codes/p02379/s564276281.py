# Distance

points = [float(i) for i in input().rstrip().split()]
a = [points[0], points[1]]
b = [points[2], points[3]]

distanceSquare = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
distance = distanceSquare ** 0.5

print(distance)

