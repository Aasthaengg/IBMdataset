import sys
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

#n = int(stdin.readline().rstrip())
#l = list(map(int, stdin.readline().rstrip().split()))

#numbers = [[int(c) for c in l.strip().split()] for l in sys.stdin]
#word = [stdin.readline().rstrip() for _ in range(n)]
#number = [[int(c) for c in stdin.readline().rstrip()] for _ in range(n)]
#zeros = [[0] * w for i in range(h)]


def main():
    R,G,B,N = map(int, stdin.readline().rstrip().split())
    ans = 0
    for r in range(N//R+1):
        for g in range((N-(r*R))//G + 1):
            b = (N - R*r - G*g) / B
            if b%1==0 and b>=0:
                ans += 1
    print(ans)

main()
