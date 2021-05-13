from sys import stdin, setrecursionlimit as srl
from threading import stack_size, Thread
from math import *
from collections import *
from heapq import *

srl(int(1e9)+7)
stack_size(int(1e8))

'''
deque
1) append
2) appendleft
3) pop
4) popleft
5) insert, remove, index, count, extend, extendleft, reverse
6) rotate           # negative value rotates to the left , positive to the right
'''

'''
heapq

minheap by default but can be used as maxheap by pushing elements after multiplying them with -1

1) heapify ( iterable )
2) heappush ( heap, element)
3) heappop (heap)                   # smallest is removed
4) heappushpop (heap, element)
5) heapreplace (heap, element)      # same as heappushpop but first popped then pushed
'''

def solve():
    #start here
    n = int(input())
    h = list(map(int,input().split()))
    dp = [0 for i in range(n)]
    dp[1] = abs(h[1] - h[0])
    for i in range(2, n):
        dp[i] = min(abs(h[i]-h[i-1])+dp[i-1], abs(h[i]-h[i-2])+dp[i-2])
    print(dp[n-1])


Thread(target=solve).start()