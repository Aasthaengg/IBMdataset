import sys
import random
import itertools
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
n,k = map(int,input().split())
print(n-k+1)