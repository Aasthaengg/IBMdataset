import math
a,b,c,d=map(int, input().split())
def gcd(a,b):
    if(a%b!=0):
        return gcd(b,a%b)
    else:
        return b
def lcm(a,b):
    return a*b//gcd(a,b)

numb = b-(b//c + b//d) + (b//(lcm(c,d)))
numa = (a-1)-((a-1)//c+(a-1)//d) + ((a-1)//lcm(c,d))
print(numb-numa)
