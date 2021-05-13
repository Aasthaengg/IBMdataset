import math
f=math.factorial
N,M=map(int,input().split())
print(max(2-abs(N-M),0)*f(N)*f(M)%(10**9+7))
