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

n = ri()
ls = ril()
left = 0
s0 = 0
s1 = 0
res = 0
for right, x in enumerate(ls):
    s0 += x
    s1 ^= x
    while s0 != s1:
        s0 -= ls[left]
        s1 ^= ls[left]
        left += 1
    res += right - left + 1
print(res)