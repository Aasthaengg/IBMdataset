import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
dd = defaultdict(int)
tt = defaultdict(int)

for i in d:
    dd[i] += 1
for i in t:
    tt[i] += 1

for k, v in tt.items():
    if dd[k] < v:
        print('NO')
        exit()
print('YES')
