import math

N = int(input())


def solve():
    nn = math.ceil(N / 2)
    return nn - 1


print(solve())
