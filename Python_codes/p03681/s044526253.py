import sys
import math
input = sys.stdin.readline

N,M = list(map(int,input().split()))
big = max(N,M)
small = min(N,M)
m=1000000007

if big == small:
    print(math.factorial(big)**2*2%m)
elif big == small + 1:
    print(math.factorial(big)*math.factorial(small)%m)
else:
    print(0)
