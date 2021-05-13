import sys
from math import ceil, floor
from collections import deque, Counter, defaultdict
from fractions import gcd
input = lambda: sys.stdin.readline().rstrip()

def eprint(s):
    sys.stderr.write('DEBUG: {}'.format(s))
    return

def main():
    n,m = map(int, input().split())
    p = 1 / 2**(m)
    t = 100*(n-m) + 1900*m
    ans = 0    
    
    # 正解する確率: p
    # i回目に正解する確率: (p-1)^(i-1) * p
    print(int( (-1) * ((p-1)*t) / ((1-p)*p)))
    return

if __name__ == '__main__':
    main()