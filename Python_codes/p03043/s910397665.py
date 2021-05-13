#!/usr/bin/env python3
n,k=map(int,input().split())
odd = 0
for i in range(1,n+1):
    a=0
    while k > i*2**a:
        a+=1
    odd += 2**-a
print(odd/n)
