# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:50:08 2019

@author: Yamazaki Kenichi
"""
import functools

N, K = list(map(int,input().split()))
A = list(map(int,input().split()))
A.sort()

S = sum(A)

def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
def dfs(x,d):
    return x%d

D = make_divisors(S)
ans = 1
for d in D:
    B = list(map(functools.partial(dfs,d=d),A[:]))
    B.sort()
    l, r, tmp = 0, N-1, 0
    res = 0
    while l <= r:
        if B[l] + B[r] + tmp == d:
            res += B[l]
            tmp = 0
            l += 1
            r -= 1
        elif B[l] + B[r] + tmp < d:
            tmp = B[l] + tmp
            res += B[l]
            l += 1
        else:
            tmp = B[r] + tmp - d 
#            res += B[l]
            r -= 1
#        print(l,r,tmp,res)
    if res <= K and d > ans:
        ans = d
print(ans)
