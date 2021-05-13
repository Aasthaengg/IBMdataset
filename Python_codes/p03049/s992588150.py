# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque

INF = 1 << 50



def run():
    N = int(input())
    S = [input() for _ in range(N)]
    countA = 0
    countB = 0
    countBA = 0
    countAB = 0
    for s in S:
        countAB += s.count('AB')
        #print(s, s.count('AB'))
        if s[0] == 'B':
            if  s[-1] == 'A':
                countBA += 1
            else:
                countB += 1
        elif s[-1] == 'A':
            countA += 1

    #print(countA, countB, countBA, countAB)
    if countBA > 1:
        countAB += countBA - 1
        countBA = 0

        if countA > 0:
            countAB += 1
            countA -= 1
        if countB>0:
            countAB += 1
            countB -= 1

    plus = min(countA, countB)

    countAB += plus
    countA -= plus
    countB -= plus

    plus = min(countBA, countA)
    countAB += plus
    countBA -= plus
    countA -= plus

    plus = min(countBA, countB)
    countAB += plus

    print(countAB)






if __name__ == "__main__":
    run()