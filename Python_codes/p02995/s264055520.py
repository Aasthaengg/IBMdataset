a,b,c,d=map(int,input().split())
from math import gcd
ans=0
def main(n):
    e=n//c+n//d-n//((c*d)//gcd(c,d))
    return n-e

print(main(b)-main(a-1))
