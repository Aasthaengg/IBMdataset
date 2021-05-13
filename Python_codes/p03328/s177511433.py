from itertools import accumulate, tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


a, b = map(int, input().split())

towers = list(accumulate(range(1, 1000)))

for p, n in pairwise(towers):
    if n - p == b - a:
        print(p - a)
        break
