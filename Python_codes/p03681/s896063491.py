from math import *
N,M = map(int,input().split())
print(max(0,2-abs(N-M))*factorial(N)*factorial(M)%(10**9+7))