import math

def prime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,math.ceil(n**0.5)+1,2):
        if n%i==0:
            return False
    
    return True

X=int(input())
while True:
    if prime(X):
        print(X)
        break
    else:
        X+=1