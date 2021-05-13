#

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N, K = map(int, input().split())
    rest = N - K
    if K == 1:
        print(0)
    else:
        print(rest)

if __name__ == '__main__':
    main()
