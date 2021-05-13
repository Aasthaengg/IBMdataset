#!/usr/bin/env python3

n,k=map(int,input().split())


if k==1:
    print(0)
elif n==k:
    print(0)
elif n>k:
    print(n-k)
else:
    print(1)

