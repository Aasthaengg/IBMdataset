#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N,M,Q = map(int, input().split())
    pair = []
    for i in range(Q):
        pair += list(map(int, input().split())),

    def score(A):
        nonlocal pair
        sum = 0
        for a,b,c,d in pair:
            if A[b-1] - A[a-1] == c:
                sum += d
        return sum

    ans = 0
    A = [1]*N
    i = N-1
    while True:
        ans = max(ans, score(A))
        while i >= 0 and A[i] == M:
            i -= 1
        if i < 0:
            break
        A[i] += 1
        j = i
        while i <= N-1:
            A[i] = A[j]
            i += 1
        i = N-1
        if A == [M]*N:
            break
        
    print(ans)
main()
