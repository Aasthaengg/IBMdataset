from itertools import accumulate
from bisect import bisect_left
import sys
readlines = sys.stdin.buffer.readlines
readline = sys.stdin.buffer.readline

N = int(readline())

memo = [None]*N

for i,s in enumerate(readlines()):
    s = s.rstrip().decode()
    memo[i] = (min(0,min(accumulate(1 if c =='(' else -1 for c in s))),sum(1 if c =='(' else -1 for c in s))



positives = sorted((m,d) for m,d in memo if d >= 0)
negatives = sorted((m-d,-d) for m,d in memo if d < 0)

def solve():
    left = 0
    for m,d in reversed(positives):
        if left+m < 0:
            return False
        left += d
    right = 0
    for m,d in reversed(negatives):
        if right+m < 0:
            return False
        right += d
    return left == right

print('Yes' if solve() else 'No')

