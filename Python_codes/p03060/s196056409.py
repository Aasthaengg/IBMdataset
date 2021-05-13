import sys
from itertools import accumulate
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
s = 0
for i in range(n):
    if a[i] >= b[i]:
        s += a[i]-b[i]
print(s)
