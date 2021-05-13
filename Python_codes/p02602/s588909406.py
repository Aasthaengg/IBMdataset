from heapq import *
import sys
from collections import *
from itertools import *
from decimal import *
import copy
from bisect import *
import math
sys.setrecursionlimit(4100000)
def gcd(a,b):
    if(a%b==0):return(b)
    return (gcd(b,a%b))
input=lambda :sys.stdin.readline().rstrip()

N,K=map(int,input().split())
A=list(map(int,input().split()))
for i in  range(K,N):
    print("Yes" if A[i]>A[i-K] else "No")
