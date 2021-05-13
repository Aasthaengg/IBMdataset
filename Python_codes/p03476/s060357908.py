import math

def is_prime(n:int):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

all=[0]+[0]*(10**5+1)
for i in range(3,10**5):
    if is_prime((i)) and is_prime((i+1)//2) :
        all[i]=all[i-1]+1
    else:
        all[i]=all[i-1]



q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print(all[r]-all[l-1])