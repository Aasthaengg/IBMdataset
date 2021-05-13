import math


def actual(a, b):
    mean = (a + b) / 2

    return math.ceil(mean)

a, b = map(int, input().split())
print(actual(a, b))