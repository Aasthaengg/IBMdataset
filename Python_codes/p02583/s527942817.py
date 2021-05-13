n = int(input())
L = list(map(int, input().split()))

import itertools
cnt = 0
for s, t, u in itertools.combinations(L, 3):
    if (s != t) and (t != u) and (u != s):
        if (s+t > u) and (t+u > s) and (s+u > t):
            cnt += 1

print(cnt)