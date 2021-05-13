import sys
#import time
#from collections import deque, Counter, defaultdict
#from fractions import gcd
#import bisect
#import heapq
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))
n = ri()
li=[rl() for _ in range(n)]
li.sort(key=lambda x: x[1])
sum_=0
for i in range(n):
    sum_+=li[i][0]
    if sum_>li[i][1]:
        print("No")
        sys.exit()
print("Yes")