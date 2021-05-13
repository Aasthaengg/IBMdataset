from itertools import combinations

n, a, q, ms = int(input()), list(map(int, input().split())), input(), map(int, input().split())

cache = {}


def sum_a(tmp, t):
    global a, cache
    if t in cache:
        return tmp + cache[t]
    elif len(t) == 1:
        return tmp + a[t[0]]
    else:
        cache[t] = result = sum_a(tmp + a[t[0]], t[1:])
        return result


l = list(sum_a(0, t) for i in range(n) for t in combinations(range(n), i + 1))

for m in ms:
    print('yes' if m in l else 'no')