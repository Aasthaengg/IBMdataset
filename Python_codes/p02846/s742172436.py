import sys

read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines


# rstrip().decode('utf-8')
# INF=float("inf")
#MOD=10**9+7
# sys.setrecursionlimit(2147483647)
# import math
#import numpy as np
# import operator
#import bisect
# from heapq import heapify,heappop,heappush
#from math import gcd
# from fractions import gcd
#from collections import deque
#from collections import defaultdict
# from collections import Counter
#from itertools import accumulate
# from itertools import groupby
# from itertools import permutations
# from itertools import combinations
# from scipy.sparse import csr_matrix
# from scipy.sparse.csgraph import floyd_warshall
# from scipy.sparse.csgraph import csgraph_from_dense
# from scipy.sparse.csgraph import dijkstra
# map(int,input().split())


def main():
	t1,t2=map(int,input().split())
	a1,a2=map(int,input().split())
	b1,b2=map(int,input().split())
	
	a=a1*t1
	aa=a2*t2
	b=b1*t1
	bb=b2*t2
	
	if a+aa==b+bb:
		print("infinity")
		exit(0)
	elif a<b and a+aa<b+bb:
		print(0)
		exit(0)
	elif a > b and a+aa > b+bb:
		print(0)
		exit(0)
	
	else:
		x=abs(a-b)
		y=abs((a+aa)-(b+bb))
		print((x//y)*2+1-(x%y==0))
		
	
	
	
	
	
	
	

	
if __name__ == "__main__":
		main()
