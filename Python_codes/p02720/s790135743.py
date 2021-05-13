import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy

if __name__ == "__main__":
    k = int(input())
    q = collections.deque([])
    for i in range(1,10):
        q.append(i)
    for i in range(k-1):
        x = q.popleft()
        if x%10 != 0:
            q.append(10*x + x%10 -1)
        q.append(10*x + x%10)
        if x%10 != 9:
            q.append(10*x + x%10 +1)
    print(q.popleft())