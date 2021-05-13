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
    H, W, K = MI()
    cake = [[s for s in input()] for h in range(H)]

    cursor = 0
    skip_rows = False
    for h in range(H):
        if '#' in cake[h]:
            cursor += 1
            first_flag = True
            for w in range(W):
                if cake[h][w] == '.':
                    cake[h][w] = cursor
                else:
                    if first_flag:
                        cake[h][w] = cursor
                        first_flag = False
                    else:
                        cursor += 1
                        cake[h][w] = cursor
            last_row = h
        else:
            skip_rows = True

    if skip_rows:
        if last_row < H - 1:
            for h in range(last_row + 1, H):
                cake[h] = cake[last_row]
        for h in range(H - 2, -1, -1):
            if '.' in cake[h]:
                cake[h] = cake[h + 1]

    for row in cake:
        row = [str(e) for e in row]
        print(' '.join(row))
        
    
if __name__ == "__main__":
    main()