import math

menu = [int(input()) for i in range(5)]
remain = [l % 10 for l in menu]

if sum(remain) == 0:
    print(sum(menu))
else:
    cost = [math.ceil(l / 10) for l in menu]
    for i in range(5):
        if remain[i] == 0:
            remain[i] = 10
    print(10 * sum(cost) - 10 + remain[remain.index(min(remain))])