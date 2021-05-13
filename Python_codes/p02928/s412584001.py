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

    N, K = NMI()
    A = NLI()
    
    cnt = 0
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i] > A[j]:
                cnt += 1
    
    repeat = 0
    ls = [0 for _ in range(len(A))]
    for k in range(len(A)):
        repeat += len([x for x in A if x < A[k]])

    
    print((cnt*K + repeat * (((K-1)*K)//2))%MOD)


if __name__ == '__main__':
    main()