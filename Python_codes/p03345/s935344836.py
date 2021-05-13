# -*- coding: utf-8 -*-

'''
A, B, C, K = map(int, input().split()) 

for i in range(K):
    a = A
    b = B
    c = C

    A = b + c
    B = a + c
    C = a + b

ans = A - B

if ans >= 10**8:
    ans = 'Unfair'
elif ans >*10**8:
    ans = 'Unfair'

print(ans)
'''



A, B, C, K= map(int, input().split())

if K%2==1: 
    ans = B - A
else:
    ans = A - B

if ans >= 10**18 or (-1)*ans >= 10**18:
    ans = 'Unfair'

print(ans)  

