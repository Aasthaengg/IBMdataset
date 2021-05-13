ma = lambda :map(int,input().split())
ni = lambda:int(input())
import collections
import math
import itertools
import heapq as hq
gcd = math.gcd
n = ni()
D = list(ma())
D.sort()
print(D[n//2] - D[(n-1)//2])