import sys
#import string
#from collections import defaultdict, deque, Counter
#import bisect
#import heapq
#import math
#from itertools import accumulate
#from itertools import permutations as perm
#from itertools import combinations as comb
#from itertools import combinations_with_replacement as combr
#from fractions import gcd
#import numpy as np

stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)
MIN = -10 ** 9
MOD = 10 ** 9 + 7
INF = float("inf")
IINF = 10 ** 18

def solve():
    #n = int(stdin.readline().rstrip())
    n,k = map(int, stdin.readline().rstrip().split())
    #l = list(map(int, stdin.readline().rstrip().split()))
    #ab = [[int(c) for c in l.strip().split()] for l in sys.stdin]
    #word = [stdin.readline().rstrip() for _ in range(n)]
    #number = [[int(c) for c in stdin.readline().rstrip()] for _ in range(n)]
    #zeros = [[0] * w for i in range(h)]
    a = [0]*(10**5+1)
    m = 0
    for i in range(n):
        A,B = map(int, stdin.readline().rstrip().split())
        a[A] += B
        m = max(m,A)
    j = 0
    for i in range(10**5):
        j += a[i]
        if j >= k:
            print(i)
            exit()
    print(m)



if __name__ == '__main__':
    solve()
