import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,k = map(int, input().split())
h = []
d = defaultdict(int)
cnt = []
for i in range(n):
    x = int(input())
    h.append(x)
    d[x] += 1

for i in d.items():
    if i[1] >= k:
        print(0)
        exit()

sh = sorted(h)
ans = 1000000001
for i in range(0, n - k + 1):
    ans = min(ans, sh[i + k - 1] - sh[i])
print(ans)
