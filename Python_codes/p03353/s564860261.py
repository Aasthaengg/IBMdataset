import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log, log2
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
#from decimal import *

def main():
	s = input()
	K = INT()

	strings = set()
	for  i in range(1, K+1): #文字列の長さ : K番目で長さがK以上のを考える必要はない。
		for j in range(len(s)-i+1): #スタート地点
			#print(j, i)
			strings.add(s[j:j+i])

	print(sorted(strings)[K-1])

if __name__ == '__main__':
	main()
