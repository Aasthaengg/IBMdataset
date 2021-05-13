N, A, B = map(int, input().split())
V = list(map(int, input().split()))

items = V[:]

items = sorted(items, reverse=True)
sub_items = items[:A]
ave = sum(sub_items)/len(sub_items)
rest_items = items[A:]

import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if ave != sub_items[0]:
    # nCr
    r = sub_items.count(sub_items[-1])
    n = rest_items.count(sub_items[-1]) + r
    pattern = combinations_count(n, r)
else:
    n = items.count(ave)
    pattern = 0
    for r in range(A, min(n+1, B+1)):
        pattern += combinations_count(n, r)


print(ave)
print(pattern)

