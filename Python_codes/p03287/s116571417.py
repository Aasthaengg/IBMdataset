import collections
import sys

input = sys.stdin.readline

ri = lambda: int(input())
rs = lambda: input().rstrip()
ril = lambda: list(map(int, input().split()))
rsl = lambda: input().rstrip().split()
ris = lambda n: [ri() for _ in range(n)]
rss = lambda n: [rs() for _ in range(n)]
rils = lambda n: [ril() for _ in range(n)]
rsls = lambda n: [rsl() for _ in range(n)]

n, m = ril()
ls = ril()
acc = [0]
counter = collections.Counter()
res = 0
for x in ls:
    counter[acc[-1]] += 1
    acc.append((acc[-1] + x) % m)
    res += counter[acc[-1]]
print(res)