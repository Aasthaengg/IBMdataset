import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
M,N=map(int,input().split())
print(N*(N-1)//2+M*(M-1)//2)