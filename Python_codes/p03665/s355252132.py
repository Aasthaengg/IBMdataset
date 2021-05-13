from math import factorial
from collections import Counter
def nCr(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))
N,P=map(int,input().split())
A=list(map(lambda x:int(x)%2,input().split()))
c=Counter(A)
z=pow(2,c.get(0,0))
res=0
for i in range(1 if P else 0,c.get(1,0)+1,2):
    res+=nCr(c.get(1,0),i)
print(z*res)