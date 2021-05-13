# ANSHUL GAUTAM
# IIIT-D

from math import *
from copy import *					# ll = deepcopy(l)
from heapq import *					# heappush(hp,x)
from string import *				# alpha = ascii_lowercase
from random import *				# l.sort(key=lambda l1:l1[0]-l1[1]) => ex: sort on the basis difference
from bisect import *				# bisect_left(arr,x,start,end)  => start and end parameters are temporary
from sys import stdin				# bisect_left return leftmost position where x should be inserted to keep sorted
from sys import maxsize				# minn = -maxsize
from operator import *				# d = sorted(d.items(), key=itemgetter(1))
from itertools import *				# pre = [0] + list(accumulate(l))
from decimal import Decimal 		# a = Decimal(a)	# use this for math questions
from collections import Counter		# d = dict(Counter(l))
from collections import defaultdict # d = defaultdict(list)

'''
3
1 2 3
'''

def solve(l,n):
	m = len(l)
	d = dict(Counter(l))
	dp = [0]*(n+1)
	dp[0] = 1
	mod = 10**9 + 7
	if(1 not in d):
		dp[1] = 1
	for i in range(2,n+1):
		if(i not in d):
			dp[i] = dp[i-1] + dp[i-2]
			dp[i] %= mod
	return dp[n]

N,M = list(map(int, stdin.readline().rstrip().split()))
l = []
for m in range(M):
	l.append(int(input()))
ans = solve(l,N)
print(ans)

