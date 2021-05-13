import os
import sys

from collections import Counter

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


N = int(sys.stdin.buffer.readline())


def solve(N, group_cnt=2):
    s = sum(range(N + 1))

    while s * (group_cnt - 1) % group_cnt != 0:
        group_cnt += 1

    groups = [set() for _ in range(group_cnt)]
    sums = [[0, i] for i in range(group_cnt)]

    for n in reversed(range(1, N + 1)):
        for i, (_, v) in enumerate(sums[1:], start=1):
            sums[i][0] -= n
            groups[v].add(n)
        sums.sort()

    # わからない。グループ数増やしていけばどっかでうまくいくらしい。
    if len(Counter([s for s, _ in sums])) > 1:
        return solve(N, group_cnt + 1)

    ans = set()
    for group in groups:
        for v in set(range(1, N + 1)) - group:
            for u in group:
                ans.add((min(v, u), max(v, u)))
    return ans


ans = solve(N)
print(len(ans))
for r in ans:
    print(*r)
exit()

for n in range(3, 101):
    ans = solve(n)

    graph = [[] for _ in range(n + 1)]
    for v, u in ans:
        graph[v].append(u)
        graph[u].append(v)

    c = Counter([sum(vs) for vs in graph[1:]])
    if len(c) > 1:
        print(n, c)
