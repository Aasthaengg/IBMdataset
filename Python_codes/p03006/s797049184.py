import math
import collections
import fractions
import itertools

def solve():
    n = int(input())
    xy = [[int(x) for x in input().split()] for _ in range(n)]
    vec = list()
    for xy1, xy2 in itertools.combinations(xy, 2):
        p = xy2[0] - xy1[0]
        q = xy2[1] - xy1[1]
        vec.append((p, q))
        vec.append((-p, -q))
    c = collections.Counter(vec)
    if n >= 2:
        ans = max(c.values())
        print(n - ans)
    else:
        print(1)
    return 0

if __name__ == "__main__":
    solve()
