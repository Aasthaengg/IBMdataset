import sys

[N] = [int(x) for x in sys.stdin.readline().strip().split(" ")]

result = 0

base = 1  # 1, 100, 10000, ...
upper = 10  # 10, 1000, 100000, ...

while base <= N:
    _upper = min(upper, N + 1)
    result += _upper - base
    base *= 100
    upper *= 100

print(result)
