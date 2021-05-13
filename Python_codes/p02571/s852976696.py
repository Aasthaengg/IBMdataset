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
    s = str(stdin.readline().rstrip())
    t = str(stdin.readline().rstrip())
    #l = list(map(int, stdin.readline().rstrip().split()))
    #numbers = [[int(c) for c in l.strip().split()] for l in sys.stdin]
    #word = [stdin.readline().rstrip() for _ in range(n)]
    #number = [[int(c) for c in stdin.readline().rstrip()] for _ in range(n)]
    #zeros = [[0] * w for i in range(h)]
    ans = len(t)
    for i in range(len(s)-len(t) + 1):
        test = s[i:i+len(t)]
        a = len(t)
        for j in range(len(t)):
            if test[j] == t[j]:
                a -= 1
        ans = min(ans,a)
    print(ans)

if __name__ == '__main__':
    solve()
