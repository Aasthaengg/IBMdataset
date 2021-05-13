#Macで実行する時
import sys
import os
if sys.platform=="darwin":
	base = os.path.dirname(os.path.abspath(__file__))
	name = os.path.normpath(os.path.join(base, '../atcoder/input.txt'))
	#print(name)
	sys.stdin = open(name)

from math import factorial

def combinations_count(n,r):
    if n < r:
        return 0
    else:
        return factorial(n) // ( factorial(n-r) * factorial(r))

n,m = map(int,input().split())

#print(combinations_count(n,2))
#print(combinations_count(m,2))

#print(factorial(0))

print(combinations_count(n,2) + combinations_count(m,2))




