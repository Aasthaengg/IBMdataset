from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N = int(input())
aa = inpl()
MAX = max(aa)
MIN = min(aa)
MAXind = aa.index(MAX)
MINind = aa.index(MIN)
ans_list = []

def calc_pl():
	global aa
	global ans_list

	for i in range(1,N):
		ba,na = aa[i-1],aa[i]
		if na >= ba:
			continue
		else:
			aa[i] += ba
			ans_list.append([i,i+1])

def calc_mn():
	global aa
	global ans_list

	for i in reversed(range(N-1)):
		ba,na = aa[i+1],aa[i]
		if na <= ba:
			continue
		else:
			aa[i] += ba
			ans_list.append([i+2,i+1])

if MIN<0 and 0<MAX:
	if abs(MIN) < abs(MAX):#正に揃える
		for i in range(N):
			if i == MAXind: continue
			ans_list.append([MAXind+1,i+1])
			aa[i] += MAX
		calc_pl()
	else:
		for i in range(N):
			if i == MINind: continue
			ans_list.append([MINind+1,i+1])
			aa[i] += MIN
		calc_mn()
elif 0 <= MIN:
	calc_pl()
elif MAX <= 0:
	calc_mn()

print(len(ans_list))
for azu,nyan in ans_list:
	print(azu,nyan)
