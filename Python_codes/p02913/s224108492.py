import sys
input = sys.stdin.readline
from collections import *

def judge(x):
    d = defaultdict(int)
    
    for i in range(N-x+1):
        k = S[i:i+x]
        
        if k in d:
            if i>=d[k]+x:
                return True
        else:
            d[k] = i
    
    return False

def binary_search():
    l, r = 0, N
    
    while l<=r:
        m = (l+r)//2
        
        if judge(m):
            l = m+1
        else:
            r = m-1
    
    return r

N = int(input())
S = input()[:-1]
print(binary_search())
