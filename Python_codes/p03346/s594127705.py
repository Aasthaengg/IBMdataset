import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    N = int(input())
    P = [0] * N
    index = [0] * (N + 1)

    for i in range(N):
        P[i] = int(input())
        index[P[i]] = i

    length = 1
    seq = 1
    for i in range(1, N):
        if index[i] < index[i + 1]:
            seq += 1
        else:
            length = max(length, seq)
            seq = 1
            
    length = max(length, seq)

    print(N - length)

sol()
