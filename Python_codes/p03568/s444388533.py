#!/usr/bin/env python3
n,*a=map(int,open(0).read().split())
e = sum(i%2 < 1 for i in a) 
print(3**n - 2**e)
