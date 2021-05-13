from collections import defaultdict
n, m = map(int, input().split())
cnt = defaultdict(int)
for _ in range(m):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1

if all(v % 2 == 0 for v in cnt.values()):
    print('YES')
else:
    print('NO')