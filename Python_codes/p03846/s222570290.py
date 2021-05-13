import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9+7
n = int(input())
a = list(map(int,input().split()))

if n%2 == 0:
    c = collections.Counter(a)
    item = []
    for key,value in c.items():
        item.append([key,value])
    item.sort()
    ans = 1
    for i in range(len(item)):
        if 2*i + 1 == item[i][0]:
            if item[i][1] == 2:
                ans *= 2
                ans %=MOD
            else:
                print(0)
                sys.exit()
        else:
            print(0)
            sys.exit()
    print(ans%MOD)
else:
    c = collections.Counter(a)
    ans = 1
    item = []
    for key,value in c.items():
        item.append([key,value])
    item.sort()
    for i in range(1,len(item)):
        if 2*i == item[i][0]:
            if item[i][1] == 2:
                ans *= 2
                ans %=MOD
            else:
                print(0)
                sys.exit()
        else:
            print(0)
            sys.exit()
    if item[0][0] == 0 and item[0][1] == 1:
        print(ans%MOD)
    else:
        print(0)