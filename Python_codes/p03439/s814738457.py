from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N = inp()

def query(x):
	print(x)
	sex = input()
	if sex == 'Male':
		return True
	elif sex == 'Female':
		return False
	else:
		print(x)
		sys.exit()


l,r = 0,N
ls = rs = query(0)

while True:
	mid = (l+r)//2
	ms = query(mid)

	if (mid-l+1)%2 == 1 and ls != ms:
		r = mid
		rs = ms
	elif (mid-l+1)%2 == 0 and ls == ms:
		r = mid
		rs = ms
	elif (r-mid+1)%2 == 1 and rs != ms:
		l = mid
		ls = ms
	elif (r-mid+1)%2 == 0 and rs == ms:
		l = mid
		ls = ms
