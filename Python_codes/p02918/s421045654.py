import sys
input=sys.stdin.readline
#from collections import defaultdict
#d = defaultdict(int)
#import fractions
#import math
#import collections
#from collections import deque
#from bisect import bisect_left
#from bisect import insort_left
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
#import itertools
#import heapq
#import numpy as np
def rle(s):#計算量N
    c = 0
    tmp, count, ans = s[0], 1, []
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans.append((-1)*count)
            c += count-1
            count = 1
            tmp = s[i]
    if count > 1:
        ans.append(count*(-1))
        c += count-1
    return ans,c #最大2N文字
N,K = map(int,input().split())
S = input()
ans,c = rle(S)
n = len(ans)
import heapq
heapq.heapify(ans)
MIN = min(n,K)
for i in range(MIN):

    a = heapq.heappop(ans)
    c += 2
if c >= N:
    c = N-1
print(c)
