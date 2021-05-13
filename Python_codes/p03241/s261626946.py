def __gcd__(m,n):
    x,y=max(m,n),min(m,n)
    if x%y==0:
        return y
    else:
        while x%y!=0:
            z=x%y
            x,y=y,z
        else:
            return z
        
from functools import reduce
def GCD(*X):
    return reduce(__gcd__,X)

N,M=map(int,input().split())

Q=M//N
R=M%N

for i in range(Q,0,-1):
    if M%i==0:
        print(i)
        break
