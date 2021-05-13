from collections import defaultdict
n, m = map(int, input().split())
cnt = defaultdict(int)
for _ in range(m):
    a, b = map(int, input().split())
    cnt[a] ^= 1
    cnt[b] ^= 1

if any(v for v in cnt.values()):
    print('NO')
else:
    print('YES')