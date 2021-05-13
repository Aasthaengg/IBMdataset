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

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def main():
    N = NI()
    
    ls = []
    
    for n in range(1,55556):
        if is_prime(n):
            if n%5 == 1:
                ls.append(n)
                if len(ls) == N:
                    print(" ".join(list(map(str,ls))))
                    break
        

if __name__ == '__main__':
    main()