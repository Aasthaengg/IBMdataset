import sys
input = sys.stdin.readline
from bisect import bisect_left

n, res = int(input()), 0
s = sorted(list(map(int, input().split())))
for i in range(n-1):
    for j in range(i+1, n):
        res += (bisect_left(s, s[i] + s[j])) - (j + 1)
print(res)