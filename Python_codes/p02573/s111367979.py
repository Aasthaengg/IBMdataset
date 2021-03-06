import sys
from collections import defaultdict as dd
from collections import deque
from functools import *
from fractions import Fraction as f
from copy import *
from bisect import *	
from heapq import *
#from math import *
from itertools import permutations ,product
 
def eprint(*args):
    print(*args, file=sys.stderr)
zz=1
 
#sys.setrecursionlimit(10**6)
if zz:
	input=sys.stdin.readline
else:	
	sys.stdin=open('input.txt', 'r')
	sys.stdout=open('all.txt','w')
def inc(d,c):
	d[c]=d[c]+1 if c in d else 1
def bo(i):
	return ord(i)-ord('A')	
def li():
	return [int(xx) for xx in input().split()]
def fli():
	return [float(x) for x in input().split()]	
def comp(a,b):
	if(a>b):
		return 2
	return 2 if a==b else 0		
def gi():	
	return [xx for xx in input().split()]
def fi():
	return int(input())
def pro(a): 
	return reduce(lambda a,b:a*b,a)		
def swap(a,i,j): 
	a[i],a[j]=a[j],a[i]	
def si():
	return list(input().rstrip())	
def mi():
	return 	map(int,input().split())			
def gh():
	sys.stdout.flush()
def isvalid(i,j):
	return 0<=i<n and 0<=j<n	
def bo(i):
	return ord(i)-ord('a')	
def graph(n,m):
	for i in range(m):
		x,y=mi()
		a[x].append(y)
		a[y].append(x)


t=1
def find(a,i):
	if i==a[i]:
		return a[i]
	a[i]=find(a,a[i])
	return a[i]
def union(a,x,y):
	xs=find(a,x)
	ys=find(a,y)
	if xs!=ys:
		if rank[xs]<rank[ys]:
			xs,ys=ys,xs
		a[ys]=xs
		rank[xs]+=1			

while t>0:
	t-=1
	n,m=mi()
	a=[i for i in range(n+1)]
	rank=[0]*(n+1)
	for i in range(m):
		x,y=mi()
		union(a,x,y)
	d=[0]*(n+1)	
	for i in range(1,n+1):	
		a[i]=find(a,i)
		d[a[i]]+=1
	print(max(d))	

	

