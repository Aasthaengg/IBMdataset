from collections import Counter
from math import factorial


def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


n = int(input())
S = [''.join(sorted(input())) for _ in range(n)]
S_c = Counter(S)

ans = 0
for i in list(S_c.values()):
    if i != 1:
        ans += combinations_count(i, 2)

print(ans)
