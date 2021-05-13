from collections import *
from itertools import *
from bisect import *
from heapq import *
import copy
import math
from fractions import gcd
import sys
#input = sys.stdin.readline


#


#XY=[list(map(int,input().split())) for i in range(N)]

#H,Y=map(int,input().split())
#print(H*Y//2)
K=int(input())
print([1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51][K-1])
