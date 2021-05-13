import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)

S = list(readline().rstrip().decode('utf-8'))

import collections
c = collections.Counter(S)
max_c = max(c["a"], c["b"], c["c"])
min_c = min(c["a"], c["b"], c["c"])
diff = abs(max_c - min_c)
if diff <= 1:
    print('YES')
else:
    print('NO')