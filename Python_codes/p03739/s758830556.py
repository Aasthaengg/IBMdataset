from itertools import accumulate

n = int(input())
a = [int(i) for i in input().split()]


def n_op(a, p):
    s = accumulate(a)
    x = 0
    n = 0

    for si in s:
        if p and si + x <= 0:
            n += 1 - (si + x)
            x += 1 - (si + x)
        if (not p) and si + x >= 0:
            n += 1 + (si + x)
            x -= 1 + (si + x)
        p = not p

    return n


answer = min([n_op(a, True), n_op(a, False)])
print(answer)
