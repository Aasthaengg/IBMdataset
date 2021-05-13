import sys
from sys import stdin,stdout
import math
import random
import heapq
from collections import Counter
from functools import lru_cache
sys.setrecursionlimit(10**7)
#@lru_cache(maxsize=None) #for optimizing the execution time of callable objects/functions(placed above callable functions)
def mcost(arr,n,dp):
    if n==1:return 0
    if dp[n]!=-1:return dp[n]
    if n==2:
        dp[n]=abs(arr[1]-arr[0])
        return dp[n]
    elif n==3:
        dp[n]=abs(arr[0]-arr[2])
        return dp[n]
    else:
        dp[n]=min(abs(arr[n-1]-arr[n-2])+mcost(arr,n-1,dp),abs(arr[n-1]-arr[n-3])+mcost(arr,n-2,dp))
        return dp[n]


try:
    for _ in range(1):
        n=int(input())
        arr=[int(i) for i in input().split()]
        dp=[-1]*(n+1)
        print(mcost(arr,n,dp))
    
except EOFError as e:
    print(e)
