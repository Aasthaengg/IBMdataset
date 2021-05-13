
import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n,p=map(int,input().split())
A=list(map(int, input().split()))
AA = [0]*n
for i in range(n):
    if A[i]%2:
        AA[i]=1
sumA = sum(AA)
res1 = 0
for i in range(p,sumA+1,2):
    res1 += comb(sumA,i)
res0 = 2**(n-sumA)

print(res1*res0)
