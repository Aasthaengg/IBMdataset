from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    M = sum(A)
    table = set()
    i = 1
    while i * i <= M:
        if M % i == 0:
            table.add(i)
            table.add(M // i)
        i += 1

    res = 1
    for p in table:
        B = list(map(lambda x: x%p, A))
        B.sort()
        
        forward = [0]*N
        forward[0] = B[0]
        for j in range(1,N):
            forward[j] = forward[j-1] + B[j]
        
        back = [0]*N
        if B[j] != 0:
            back[N-1] = p - B[j]
        for j in reversed(range(N-1)):
            if B[j] == 0:
                back[j] = back[j+1]
            else:
                back[j] = back[j+1] + p - B[j]
        
        for j in range(N-1):
            if forward[j] == back[j+1] and forward[j] <= K:
                res = max(res, p)
    
    print(res)
        

if __name__ == '__main__':
    main()