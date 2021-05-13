import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

# 解説AC
N = int(sys.stdin.buffer.readline())

if N % 2 == 0:
    groups = [set() for _ in range(N // 2)]
    for i in range(N // 2):
        groups[i].add(i + 1)
        groups[i].add(N - i)
else:
    groups = [set() for _ in range(N // 2 + 1)]
    for i in range(N // 2):
        groups[i].add(i + 1)
        groups[i].add(N - i - 1)
    groups[-1].add(N)

ans = set()
for group in groups:
    for v in set(range(1, N + 1)) - group:
        for u in group:
            ans.add((min(v, u), max(v, u)))

print(len(ans))
for r in ans:
    print(*r)
