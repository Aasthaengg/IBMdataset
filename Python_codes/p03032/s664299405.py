n, k = map(int, input().split())
vs = [int(i) for i in input().split()]


def getv(takel, taker, drop):
    g = vs[:takel] + vs[len(vs) - taker:] + [0] * drop
    return sum(sorted(g, reverse=True)[:takel + taker])


def getm(take):
    if take >= n:
        return getv(n, 0, k - take)
    else:
        m = 0
        for takel in range(take + 1):
            m = max([m, getv(takel, take - takel, k - take)])
        return m


def solve():
    return max([getm(take) for take in range(k + 1)])


print(solve())
