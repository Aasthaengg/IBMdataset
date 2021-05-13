from sys import stdin
def ip(): return [int(i) for i in stdin.readline().split()]
def sp(): return [str(i) for i in stdin.readline().split()]

import math
n,x,t = ip()
c = math.ceil(n/x)
print(int(c * t))
