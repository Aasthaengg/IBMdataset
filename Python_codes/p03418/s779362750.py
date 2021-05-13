import bisect
import collections
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

N,K = map(int,(input().split()))
ans = 0
def count(n,k,b):
    return (n//b)*(b-k) + max(0,n%b-k+1 )
for b in range(K+1,N+1):
    ans += count(N,K,b) - count(0,K,b)
print(ans)