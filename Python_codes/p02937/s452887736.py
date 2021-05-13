import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, atan, degrees
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left
import heapq
import numpy as np

def input(): return sys.stdin.readline().strip()
def INt(): return int(input())
def MAP(): return map(int, input().split())
def LISt(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def main():
	s = input()
	t = input()
	
	if not set(s) >= set(t):
		print(-1)
		exit()

	dic = defaultdict(list)
	for i, char in enumerate(s):  # 文字列が出現する位置のリスト
		dic[char].append(i)
	
	loop = 0
	index = -1
	for i in range(len(t)):
		idx = bisect_left(dic[t[i]], index)  # リストの何個目とヒットするか
		if idx != len(dic[t[i]]):
			index = dic[t[i]][idx] + 1
		else:  # idx = |dic[t[i]]| -> もうヒットする箇所がないので次のループ
			loop += 1
			index = -1
			idx = bisect_left(dic[t[i]], index)
			index = dic[t[i]][idx] + 1

	print(len(s)*loop+index)

if __name__ == '__main__':
	main()
