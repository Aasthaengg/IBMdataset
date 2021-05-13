import math

x1,y1,x2,y2 = map(float, input().split())

# https://en.wikipedia.org/wiki/Euclidean_distance
dx = x1 - x2
dy = y1 - y2
print(math.sqrt(dx ** 2 + dy ** 2))
