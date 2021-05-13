import math

def Isprime(x):
    if x == 2:
        return True
    i = 2
    while(i <= math.sqrt(x)):
        if(x%i==0):
            return False
        i += 1
    return True

n = int(input())

i = 0
count = 0
while(n>i):
    a = int(input())
    if(Isprime(a)==True):
        count += 1
    i += 1
print(count)