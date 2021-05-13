n = int(input())
s = list(map(int, input().split()))


def cost(t):
    res = 0
    sum = 0
    for y in s:
        sum += y
        if sum * t <= 0:
            res += abs(sum - t)
            sum = t
        t *= -1
    return res


print(min(cost(1), cost(-1)))
