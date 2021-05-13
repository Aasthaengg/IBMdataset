from math import floor
from sys import exit

def isinteger(n):
    if isinstance(n,int):
        return True
    if isinstance(n,float):
        return n.is_integer()
    return False

n = int(input())
for i in range(floor(1700*n/(7000-n)-1),floor(3*n/4)+2):
    if 14000*i != (3500+i)*n and 4*i != n:
        mini = 3500*n*i/(14000*i-(3500+i)*n)
        maxi = 2*n*i/(4*i-n)
        for j in range(floor(mini)-1,floor(maxi)+2):
            if i!=0 and j!=0 and 4/n != 1/i+1/j:
                w = 1/(4/n-1/i-1/j)
                if abs(w-round(w))<=10**(-8) and 3500>=w>=1 and j >= 1 and i >= 1:
                    exit(print(i,j,round(w)))
            else:
                continue
    else:
        continue