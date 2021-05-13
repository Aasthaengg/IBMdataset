import sys
import time
#from collections import deque, Counter, defaultdict
#from fractions import gcd
#import bisect
#import heapq
import math
start=time.time()
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))
n = rl()
a=rl()
cnt=0
for i in a:
    if i<0:
        cnt+=1
if cnt%2==0:
    print(sum(map(abs,a)))
else:
    print(sum(map(abs,a))-2*min(map(abs, a)))