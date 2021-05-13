import sys
from heapq import *
from math import ceil
from itertools import accumulate
def input(): return sys.stdin.readline().strip()


def main():
    n, h = map(int, input().split())
    cut = []
    throw = []
    for i in range(n):
        a, b = map(int, input().split())
        cut.append(a)
        throw.append(b)
    cut_max = max(cut)
    throw.sort(reverse=True)
    throw_sum = [0] + list(accumulate(throw))

    loss = set()
    ans = 10**10
    for t in range(n + 1):
        rem = max(0, h - throw_sum[t])
        ans = min(ans, t + ceil(rem / cut_max))
    print(ans)



if __name__ == "__main__":
    main()
