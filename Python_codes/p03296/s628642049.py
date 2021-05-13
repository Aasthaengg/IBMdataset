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


def rle(s):
    import itertools
    return list(map(lambda x: (x[0], len(list(x[1]))), itertools.groupby(s)))


n = ri()
ls = ril()
ls = rle(ls)
res = 0
for _, x in ls:
    res += x // 2
print(res)