from collections import Counter 
from collections import defaultdict
from collections import deque
import math
import itertools
import heapq
import sys
sys.setrecursionlimit(10**6)

#n=int(input())
#n,m=list(map(int,input().split()))
#a=list(map(int,input().split()))
input_list = lambda : list(map(int,input().split()))

n,k=input_list()
k-=1
s=[v for v in input()]

diff=ord("A")-ord("a")

s[k]=(chr(ord(s[k])-diff))
print("".join(s))