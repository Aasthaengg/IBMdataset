import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

L = list(map(int, read().decode("utf-8").split()))

import itertools
p = itertools.permutations(L, 5)
ans = INF
for dishes in p:
    tmp_ans = 0
    for i, d in enumerate(dishes):
        tmp_ans += d
        rest = 10 - (d % 10)
        if i != 4 and rest != 10:
            tmp_ans += rest
    ans = min(ans, tmp_ans)
print(ans)