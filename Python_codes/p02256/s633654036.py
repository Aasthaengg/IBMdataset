import sys
a1,b1 = list(map(int,input().split()))

def gcd(a,b):
    if(b == 0):
        return a
    else:
        c = b
        b = a%b
        a = c

        return(gcd(a,b))

print(gcd(a1,b1))