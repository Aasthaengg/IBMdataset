from sys import exit
import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

h,n = mi()
a = li()

if h <= sum(a):
    print('Yes')
else:
    print('No')