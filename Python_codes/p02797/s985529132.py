# coding: utf-8
import math
n, k, s = map(int,input().split())
#T = list(map(int,input().split()))
A = [str(s)] * k
if s==10**9:
    A += [str(s-1)] * (n-k)
else:
    A += [str(s+1)] * (n-k)
    
print(' '.join(A))