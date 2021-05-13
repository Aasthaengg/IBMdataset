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

s = rs()
k = ri()
ss = set()
n = len(s)
for i in range(n):
    for j in range(1, 6):
        ss.add(s[i:i + j])
print(sorted(ss)[k - 1])