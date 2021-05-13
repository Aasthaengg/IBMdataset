import sys
input = sys.stdin.readline
from collections import *

def judge(x):
    cnt = 0
    
    for hi in h:
        cnt += max(0, (hi-B*x+A-B-1)//(A-B))
    
    return cnt<=x

def binary_search():
    l, r = 0, 10**10
    
    while l<=r:
        m = (l+r)//2
        
        if judge(m):
            r = m-1
        else:
            l = m+1
    
    return l

N, A, B = map(int, input().split())
h = [int(input()) for _ in range(N)]
print(binary_search())