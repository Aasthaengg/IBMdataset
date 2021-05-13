a,b,c,d=map(int,input().split())
from math import *
f=lambda x:x-x//c-x//d+x//(c*d//gcd(c,d))
print(f(b)-f(a-1))