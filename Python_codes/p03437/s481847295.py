def solve(x, y):
    for k in range(1, 1000):
        r = k * x
        if r % y != 0:
            return r
    return -1
x, y = map(int, input().split())
print(solve(x, y))
