import sys
read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs= sys.stdin.buffer.readlines
#rstrip().decode('utf-8')

#import math
#import numpy as np
#import operator
#import bisect
#from heapq import heapify,heappop,heappush
#from math import gcd
#from fractions import gcd
from collections import deque
#from collections import defaultdict
#from collections import Counter
#from itertools import accumulate
#from itertools import groupby
#from itertools import permutations
#from itertools import combinations
#from scipy.sparse import csr_matrix
#from scipy.sparse.csgraph import floyd_warshall
#from scipy.sparse.csgraph import csgraph_from_dense
#from scipy.sparse.csgraph import dijkstra
#sys.setrecursionlimit(10**7)

#map(int,input().split())

def main():
	n,m=map(int,input().split())
	li=[[] for _ in range(n+1)]
	for i in range(m):
		l,r,d=map(int,input().split())
		li[l].append((r,d))
		li[r].append((l,-d))
	
	q=deque()
	a=[None]*(n+1)

	for i in range(1,n+1):
		if a[i]==None:
			q=[i]
			a[i]=0
			while q:
				now=q.pop()
				for r,d in li[now]:
					if a[r]==None:
						a[r] = a[now] + d
						q.append(r)
					else:
						if a[r]-a[now]!=d:
							print("No")
							exit(0)
						else:
							continue
					
	print("Yes")
	
	
if __name__ == '__main__':
	main()