import sys
import itertools
sys.setrecursionlimit(10000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy

if __name__ == "__main__":
    s = input()
    t = input()
    ans = 10**9
    for i in range(len(s)-len(t)+1):
        cnt = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                cnt+=1
        ans = min(ans,cnt)
    print(ans)