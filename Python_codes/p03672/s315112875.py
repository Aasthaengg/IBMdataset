import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    S = input()

    ans = 0
    for i in range(len(S)):
        S_tmp = S[:-i-1]
        if len(S_tmp)%2 != 0:
            continue
        ci = len(S_tmp)//2
        if S_tmp[:ci] == S_tmp[ci:]:
            ans = max(ans, len(S_tmp))
    print(ans)


if __name__ == '__main__':
    main()
