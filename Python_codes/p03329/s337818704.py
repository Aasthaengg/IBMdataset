N=int(input())
from itertools import product
a=10**5
for p in product(range(9),repeat=5):
    n=N-sum([9**(i+1)*p[i] for i in range(5)])
    if n<0:continue
    b=sum(p)
    x=6**6
    while x>0:
        b+=n//x
        n%=x
        x//=6
    a=min(a,b)
print(a)