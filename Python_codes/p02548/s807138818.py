import sys
from sys import stdin,stdout
import math
import random
import heapq
from collections import Counter
from functools import lru_cache
#@lru_cache(maxsize=None) #for optimizing the execution time of callable objects/functions(placed above callable functions)




try:
    for _ in range(1):
        n=int(input())
        ans=0
        for i in range(1,n+1):
            ans+=(n-1)//i
        print(ans)
            



    
except EOFError as e:
    print(e)
