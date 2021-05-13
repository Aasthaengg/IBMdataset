# ABC047 C 一次元リバーシ

import itertools

s = itertools.groupby(list(input()))

ans = 0
for _ in s:
    ans += 1

print(ans - 1)