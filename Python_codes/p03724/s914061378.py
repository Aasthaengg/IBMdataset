from collections import defaultdict
import sys
input = sys.stdin.readline


count = defaultdict(int)
n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    count[a] += 1
    count[b] += 1

for cnt in count.values():
    if cnt % 2 != 0:
        print('NO')
        exit()

print('YES')
