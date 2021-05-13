from itertools import product

N, M = map(int, input().split())


def on_count(p):
    c = 0
    while p > 0:
        if p % 2 == 1:
            c += 1
        p //= 2
    return c


switches = []
for i in range(M):
    k, *sw = map(int, input().split())
    switches.append(sw)
P = list(map(int, input().split()))

total = 0
for pattern in product([0, 1], repeat=N):
    t = 0
    for k, indices in enumerate(switches):
        n_on = 0
        for idx in indices:
            if pattern[idx-1]:
                n_on += 1
        if n_on % 2 == P[k]:
            t += 1
    if t == M:
        total += 1
print(total)
