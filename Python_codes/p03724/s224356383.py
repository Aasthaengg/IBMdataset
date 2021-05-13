from collections import defaultdict
n, m = map(int, input().split())
cnt = defaultdict(int)
for _ in range(m):
    a, b = map(int, input().split())
    cnt[a] = (cnt[a]+1) % 2
    cnt[b] = (cnt[b]+1) % 2

if any(v for v in cnt.values()):
    print('NO')
else:
    print('YES')