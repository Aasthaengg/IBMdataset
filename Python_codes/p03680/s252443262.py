import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(10**6)
INF = 10**20

def mint():
    return map(int,input().split())
def lint():
    return map(int,input().split())

N = int(input())
a = [int(input()) for _ in range(N)]

tmp = 1
for i in range(1,N+1):
    tmp = a[tmp-1]
    if tmp==2:
        print(i)
        exit()
print(-1)