#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,sqrt
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
mod=10**9+7

h,w=MI()
lis=[LI() for i in range(h)]
pos=[0 for i in range(h*w)]
nums=[0 for i in range(h*w)]
count=0
for i in range(h):
    for j in range(w):
        if i%2==0:
            k=j
        else:
            k=w-j-1
        nums[count]=lis[i][k]
        pos[count]=[i+1,k+1]
        count+=1
#print(nums)
#print(pos)
c=0
for i in range(h*w):
    if nums[i]%2==1:
        c+=1
u=[]
for i in range(h*w-1):
    if nums[i]%2==1:
        nums[i+1]+=1
        u.append([pos[i],pos[i+1]])
        #print(*pos[i],*pos[i+1])
print(len(u))
for i in range(len(u)):
    print(*u[i][0],end=" ")
    print(*u[i][1])