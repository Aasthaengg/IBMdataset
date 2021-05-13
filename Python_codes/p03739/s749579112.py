from functools import lru_cache
n = int(input())
s = list(map(int, input().split()))


@lru_cache(maxsize=None)
def cost_e():
    res = 0
    sum = 0
    for j, y in enumerate(s, 1):
        tmp = sum + y
        if j & 1 and tmp >= 0:
            sum = -1
            res += abs(tmp) + 1
        elif not j & 1 and tmp <= 0:
            sum = 1
            res += abs(tmp) + 1
        else:
            sum = tmp
    return res


@lru_cache(maxsize=None)
def cost_o():
    res = 0
    sum = 0
    for j, y in enumerate(s, 1):
        tmp = sum + y
        if j & 1 and tmp <= 0:
            sum = 1
            res += abs(tmp) + 1
        elif not j & 1 and tmp >= 0:
            sum = -1
            res += abs(tmp) + 1
        else:
            sum = tmp
    return res


print(min(cost_e(), cost_o()))
