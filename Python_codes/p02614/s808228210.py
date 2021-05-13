from itertools import product

h, w, k = map(int, input().split())
c = [input() for _ in range(h)]


def n_black(fillh, fillw):
    n = 0
    for ih, iw in product(range(h), range(w)):
        if (not fillh[ih]) and (not fillw[iw]) and c[ih][iw] == "#":
            n += 1
    return n


answer = 0
for fillh, fillw in product(
    product([True, False], repeat=h), product([True, False], repeat=w)
):
    if n_black(fillh, fillw) == k:
        answer += 1
print(answer)
