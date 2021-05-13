# -*- coding:utf-8 -*-
def gcd(n,m):
    if n < m:
        tmp = m
        m = n
        n = tmp
    while m > 0:
        r = n % m
        n = m
        m = r
    return n
    
x, y = map(int,input().split())
print(gcd(x,y))