# coding: utf-8
# コッホ曲線
import math
import decimal


def koch(depth, p1, p2):
    if depth == 0:
        return

    s = (decimal.Decimal((2 * p1[0] + 1 * p2[0])) / 3,
         decimal.Decimal((2 * p1[1] + 1 * p2[1])) / 3)
    t = (decimal.Decimal((1 * p1[0] + 2 * p2[0])) / 3,
         decimal.Decimal(((1 * p1[1] + 2 * p2[1]))) / 3)
    u = (
        (t[0] - s[0]) * decimal.Decimal(math.cos(math.radians(60))) -
        (t[1] - s[1]) * decimal.Decimal(math.sin(math.radians(60))) + s[0],
        (t[0] - s[0]) * decimal.Decimal(math.sin(math.radians(60))) +
        (t[1] - s[1]) * decimal.Decimal(math.cos(math.radians(60))) + s[1],
    )

    koch(depth - 1, p1, s)
    print(' '.join(map(lambda x: '{:.8f}'.format(x), s)))
    koch(depth - 1, s, u)
    print(' '.join(map(lambda x: '{:.8f}'.format(x), u)))
    koch(depth - 1, u, t)
    print(' '.join(map(lambda x: '{:.8f}'.format(x), t)))
    koch(depth - 1, t, p2)


if __name__ == "__main__":
    depth = int(input())
    p1 = (decimal.Decimal(0), decimal.Decimal(0))
    p2 = (decimal.Decimal(100), decimal.Decimal(0))
    print(' '.join(map(lambda x: '{:.8f}'.format(x), p1)))
    koch(depth, p1, p2)
    print(' '.join(map(lambda x: '{:.8f}'.format(x), p2)))

