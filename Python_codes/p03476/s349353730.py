import sys
import math
import itertools
import collections
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    Q = NI()
    LR = [NLI() for _ in range(Q)]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    cumsum = [0 for _ in range((10**5)+10)]
    cnt = 0
    for n in range(1,len(cumsum)):
        cumsum[n] = cumsum[n-1]
        if is_prime(n):
            if is_prime((n+1)//2):
                cumsum[n] += 1
    
    for q in range(Q):
        print(cumsum[LR[q][1]] - cumsum[LR[q][0]-1])
    

if __name__ == '__main__':
    main()