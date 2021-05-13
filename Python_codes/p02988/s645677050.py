ma = lambda :map(int,input().split())
ni = lambda:int(input())
import collections
import math
import itertools
import heapq as hq
gcd = math.gcd
n = ni()
P = list(ma())
cnt = 0
for i in range(1,n-1):
    if P[i] >min(P[i-1],P[i+1]) and P[i] <max(P[i-1],P[i+1]):
        cnt+=1
print(cnt)
