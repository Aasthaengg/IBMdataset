import collections
import sys

N = int(input())
*D, = map(int, input().split())
M = int(input())
*T, = map(int, input().split())

d = collections.Counter(D)
t = collections.Counter(T)

for k,v in t.items():
    if d[k] >= v:
        pass
    else:
        print('NO')
        sys.exit()
print('YES')