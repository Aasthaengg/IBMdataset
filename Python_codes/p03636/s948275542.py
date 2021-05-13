import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    S = input()

    print(S[0] + str(len(S)-2) +S[-1])


if __name__ == '__main__':
    main()