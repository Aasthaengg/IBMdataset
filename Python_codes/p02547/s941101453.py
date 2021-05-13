#from collections import deque
#from heapq import heapify, heappop, heappush
#from bisect import insort
#from math import gcd
#mod = 10**9 + 7
N = int(input())
#N, K = map(int, input().split())
#A = list(map(int, input().split()))
flag1 = False
flag2 = False
flag3 = False
c, d = map(int, input().split())
if c == d:
	flag1 = True
c, d = map(int, input().split())
if c == d:
	flag2 = True
c, d = map(int, input().split())
if c == d:
	flag3 = True

k = 3
while k < N:
	if flag1 and flag2 and flag3:
		break
	k += 1
	c, d = map(int, input().split())
	flag1 = flag2
	flag2 = flag3
	if c == d:
		flag3 = True
	else:
		flag3 = False
		

#ans = 0
#print(ans)
#print('Yes')
if flag1 and flag2 and flag3:
	print('Yes')
else:
	print('No')