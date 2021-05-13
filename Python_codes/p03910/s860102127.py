import sys
#import string
#from collections import defaultdict, deque, Counter
#import bisect
#import heapq
import math
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
    n = int(stdin.readline().rstrip())
    #A, B, C = map(int, stdin.readline().rstrip().split())
    #l = list(map(int, stdin.readline().rstrip().split()))
    #numbers = [[int(c) for c in l.strip().split()] for l in sys.stdin]
    #word = [stdin.readline().rstrip() for _ in range(n)]
    #number = [[int(c) for c in stdin.readline().rstrip()] for _ in range(n)]
    #zeros = [[0] * w for i in range(h)]
    p = math.ceil(n/2)
    for i in range(n):
        num = (p*(p+1))/2
        if num <= n:
            break
        else:
            p -= 1
    if num == n:
        for i in range(p):
            print(i+1)
        exit()
    else:
        p += 1
        num = (p*(p+1))/2
        dif = num-n
        for i in range(p):
            if i+1 == dif:
                pass
            else:
                print(i +1)








if __name__ == '__main__':
    solve()
