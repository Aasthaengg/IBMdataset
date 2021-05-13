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
4
RGRBG

[0,2]
[1,4]
[3,5]
'''

def solve(s):
	n = len(s)
	r,g,b = s.count('R'),s.count('G'),s.count('B')
	sub = 0
	for i in range(n):
		for j in range(i+1,n):
			k = 2*j - i
			if(k >= n):
				break
			if(len(set([s[i],s[j],s[k]])) == 3):
				sub += 1
	return r*g*b - sub


N = int(stdin.readline())
l = input()
ans = solve(l)
print(ans)

