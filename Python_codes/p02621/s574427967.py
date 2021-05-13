from sys import stdin
input = lambda: stdin.readline().rstrip("\r\n")
from collections import defaultdict as vector, deque as que
inin = lambda: int(input())
inar = lambda: list(map(int,input().split()))
from heapq import heappush as hpush,heappop as hpop

a=inin()
print(a+a*a+a*a*a)