import math


def IsPrime(x):
    i=2
    while(i<=math.sqrt(x)):
        if(x%i==0):
            return False
        i+=1
    return True

a=[]
n=int(input())
nn=n
i=0
while(n>i):
    b=int(input())
    if(not IsPrime(b)):
        nn-=1
    i+=1
print(nn)