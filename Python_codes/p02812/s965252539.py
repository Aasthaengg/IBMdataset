import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush,heapify
from math import ceil, floor, sqrt
from copy import deepcopy


def main():
	count = 0
	num = int(input())
	strings = input()
	
	for i in range(0,num-2,1):
		if strings[i] == "A" and strings[i+1] == "B" and strings[i+2] == "C":	
			count += 1
	print(count)

if __name__ == '__main__':
	main()
