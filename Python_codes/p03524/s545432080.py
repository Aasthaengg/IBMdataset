import math
import sys

s = sys.stdin.readline().rstrip()
d = {'a': 0, "b": 0, "c": 0}
for si in s:
    if si in d:
        d[si] += 1
    else:
        d[si] = 1
x = (len(s)-1) // 3+1
if d['a'] <= x and d['b'] <= x and d['c'] <= x:
    print("YES")
else:
    print("NO")
