import sys
input = sys.stdin.readline
from collections import *

def judge(x):
    B = [x//Fi for Fi in F]
    cnt = 0
    
    for Ai, Bi in zip(A, B):
        cnt += max(0, Ai-Bi)
    
    return cnt<=K

def binary_search():
    l, r = 0, 10**14
    
    while l<=r:
        m = (l+r)//2
        
        if judge(m):
            r = m-1
        else:
            l = m+1
    
    return l

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
F = list(map(int, input().split()))
F.sort(reverse=True)
print(binary_search())