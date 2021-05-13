import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import ceil


def check(s):
    cnt = 0
    for hh in h:
        if s * b < hh:
            cnt += ceil((hh - s * b) / (a - b))
    return cnt <= s


n, a, b, *h = map(int, read().split())
low = 0
high = 10 ** 18
while low + 1 < high:
    mid = (low + high) // 2
    if check(mid):
        high = mid
    else:
        low = mid
print(high)
