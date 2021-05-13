N = int(input())

TA = [[int(_) for _ in input().split()] for _ in range(N)]

x, y = 1, 1


def ceil(a, b):
    return a // b + (a % b > 0)


for t, a in TA:
    tv = ceil(x, t)
    av = ceil(y, a)
    n = max(tv, av)
    x = n * t
    y = n * a
print(x + y)
