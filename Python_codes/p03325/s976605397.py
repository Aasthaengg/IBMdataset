#!/usr/bin/env python3

def factorization(n):
    arr = []
    temp = n
    i = 2
    cnt=0
    if temp%i==0:
        while temp%i==0:
            cnt+=1
            temp //= i
    return cnt



N = int(input())
A = list(map(int, input().split()))

ret = 0
for a in A:
    ret += factorization(a)

print(ret)
