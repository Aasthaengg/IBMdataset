import sys
def gcd(a,b):
    if a<b:
        t = a
        a = b
        b = t
    while b != 0:
        temp = b
        b = a%b
        a = temp
    return a

for i in sys.stdin:
    a,b = map(int, i.split())
    g = gcd(a,b)
    print(g, a*b//g)