# -*- coding: utf-8 -*-
import sys
import copy
import collections
from bisect import bisect_left
	
def main():
	N, i = map(int, input().split())
	
	print(N-i+1)
	
if __name__ == "__main__":
	main()
