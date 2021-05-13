# coding: utf-8
# hello worldと表示する
#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

prepare=[]
n=I()
tree=[[] for i in range(n)]
for i in range(n-1):
    a,b=MI()
    a-=1
    b-=1
    prepare.append([a,b])
    tree[a].append(b)
    tree[b].append(a)
lis=sorted(LI(),reverse=True)
answers=[0 for i in range(n)]
Q=deque([0])
answers[0]=lis[0]
count=1
while Q:
    q=Q.popleft()
    for x in tree[q]:
        if answers[x]==0:
            answers[x]=lis[count]
            Q.append(x)
            count+=1
#print(answers)
ans=0
for i in range(n-1):
    ans+=min(answers[prepare[i][0]],answers[prepare[i][1]])
print(ans)
print(*answers)