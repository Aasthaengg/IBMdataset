#! /usr/lib/python3

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

while True:
    try:
        a, b=map(int, input().split())
        s=gcd(a,b)
        print("{0} {1:.0f}".format(s,a*b/s))
    except:
        break