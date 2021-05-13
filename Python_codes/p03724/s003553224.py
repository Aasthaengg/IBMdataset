from collections import Counter
import sys
N, M = map(int, input().split())

lis = []
for m in range(M):
    a, b = map(int, input().split())
    lis.append(a)
    lis.append(b)

for value in Counter(lis).values():
    if value % 2 != 0:
        print('NO')
        sys.exit()
print('YES')