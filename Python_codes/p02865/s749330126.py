#!/usr/bin/env python3

n=int(input())

if n<=2:
    print(0)
elif n%2==0:
    print(int(n/2-1))
else:
    print(int(n/2-0.5))

