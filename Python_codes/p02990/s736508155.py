import math
n,k = map(int,input().split())

def ncr(n,r):
    f = math.factorial
    return (f(n) // f(r) // f(n-r))


for i in range(1,k+1):
    if n-k+1 < i:
        print(0)
    else:
        print(ncr(n-k+1, i) * ncr(k-1,i-1) % (10**9+7))