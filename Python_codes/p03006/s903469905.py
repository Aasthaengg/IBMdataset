from collections import defaultdict as dd
from itertools import combinations
from sys import exit
n = int(input())
if n == 1:
    print(1)
    exit()

Points = []
for i in range(n):
    Points.append(list(map(int, input().split())))

Vector = dd(lambda: 0)
for point1, point2 in combinations(Points, 2):
    if point1[0] > point2[0]:
        x_v = point1[0] - point2[0]
        y_v = point1[1] - point2[1]
    elif point1[0] == point2[0] and point1[1] >= point2[1]:
        x_v = point1[0] - point2[0]
        y_v = point1[1] - point2[1]
    else:
        x_v = point2[0] - point1[0]
        y_v = point2[1] - point1[1]
    Vector[(x_v, y_v)] += 1
#print(Vector)

print(max(n - max(Vector.values()), 1))

