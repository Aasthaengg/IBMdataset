from itertools import groupby


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


N, A, B = map(int, input().split())
if all_equal(map(lambda x: x % 2, (A, B))):
    print((B - A) // 2)
else:
    print(min((A - 1, N - B)) + 1 + (B - A - 1) // 2)
