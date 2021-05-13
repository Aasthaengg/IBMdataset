import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD2 = 998244353
INF = float('inf')
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    K, T = NMI()
    A = NLI()

    max_A = max(A)
    
    if T == 1:
        print(K-1)
    else:
        if max_A <= math.ceil(K/2):
            print(0)
        else:
            if K % 2 == 0:
                print(2*(max_A-math.ceil(K/2))-1)
            else:
                print(2*(max_A-math.ceil(K/2)))


if __name__ == '__main__':
    main()