from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


N = int(input())
A = list(map(int, input().split()))
cut = 0
previous = None
is_increase = False
is_decrease = False

for a in A:
    if previous is None:
        previous = a
    elif not (is_increase or is_decrease):
        if previous < a:
            is_increase = True
        elif previous > a:
            is_decrease = True
        previous = a
    elif is_increase and a < previous:
        cut += 1
        is_increase = False
    elif is_decrease and a > previous:
        cut += 1
        is_decrease = False

    previous = a

print(cut + 1)
