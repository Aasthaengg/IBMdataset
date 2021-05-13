import sys
from math import ceil, log2

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


n, k = nm()
p = 0
for i in range(1, n + 1):
    if i >= k:
        p += 1 / n
    else:
        num = ceil(log2(k / i))
        p += (1 / n) * (1 / pow(2, num))

print(p)