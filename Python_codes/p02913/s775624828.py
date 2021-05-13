import sys
input = sys.stdin.readline
from collections import *

def judge(x):
    d = defaultdict(int)
    q = deque([])
    
    for i in range(x):
        q.append(S[i])
        
    d[''.join(q)] = 0
    
    for i in range(x, N):
        q.append(S[i])
        q.popleft()
        k = ''.join(q)
        
        if k in d:
            if i-x+1-d[k]>=x:
                return True
        else:
            d[k] = i-x+1
    
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