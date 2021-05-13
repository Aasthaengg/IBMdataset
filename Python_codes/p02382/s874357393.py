import math

class vector():

    def __init__(self, x):
        self.x = x

def minkowski_p(x, y, p):
    s = 0

    for xi, yi in zip(x, y):
        s += abs(xi - yi) ** p

    s = s ** (1 / p)

    return s

def minkowski_infty(x, y):
    return max([abs(xi - yi) for xi, yi in zip(x, y)])

_ = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

print(minkowski_p(x, y, 1))
print(minkowski_p(x, y, 2))
print(minkowski_p(x, y, 3))
print(minkowski_infty(x, y))
