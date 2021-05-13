import bisect
import math
import sys
from collections import Counter, defaultdict, deque
from copy import copy, deepcopy
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations
from queue import Queue

read = sys.stdin.read
readline = sys.stdin.readline 
readlines = sys.stdin.readlines 

def SI():
    return int(readline())
def MI():
    return map(int, readline().split())
def MLI():
    return map(int, open(0).read().split())

inf = float("inf")


def main():
    H, W, A, B = MI()
    ret = [[0] * A + [1] * (W - A)] * B \
    	+ [[1] * A + [0] * (W - A)] * (H - B)
    for row in ret:
        row = [str(i) for i in row]
        row = ''.join(row)
        print(row)
        

if __name__ == "__main__":
    main()