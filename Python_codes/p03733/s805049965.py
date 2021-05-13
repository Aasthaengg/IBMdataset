from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


N, T = map(int, input().split())
ts = list(map(int, input().split()))
s = 0

for p, n in pairwise(ts + [ts[-1] + T]):
    if n - p >= T:
        s += T
    else:
        s += n - p
print(s)
