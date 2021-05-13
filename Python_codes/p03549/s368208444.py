from sys import stdin
import math
import bisect
import heapq
import numpy as np

n,m = [int(x) for x in stdin.readline().rstrip().split()]
print((100*(n-m)+1900*m)*2**m)