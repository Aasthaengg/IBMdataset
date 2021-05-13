import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush

def main():
    n,m = map(int, input().split())
    A = []
    B = []
    for _ in range(m):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    AB = []
    AB.extend(A)
    AB.extend(B)
    for i in range(n):
        count = 0
        for j in range(len(AB)):
            if i+1 == AB[j]:
                count += 1
        print(count)


if __name__ == '__main__':
    main()
