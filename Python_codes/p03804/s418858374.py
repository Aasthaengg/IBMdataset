# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque

def run():
    N,M = map(int, sysread().split())
    A, B = [],[]
    for i in range(N):
        A.append(input())
    for i in range(M):
        B.append(input())
    # extract candidates
    b = B[0]
    collection = []
    for i in range(N-M+1):
        a = A[i]
        for j in range(N-M+1):
            for k in range(M):
                if a[j+k] != b[k]:break
            collection.append((i,j))

    for start in collection:
        i, j = start
        breaked = False
        for x in range(M):
            if A[i+x][j:j+M] != B[x]:
                breaked = True
                break
        if not breaked:
            print("Yes")
            return None
    print("No")




if __name__ == "__main__":
    run()