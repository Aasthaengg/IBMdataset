import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readlines

import math

def main():

    lines = input()
    a, b, c, d = list(map(int, lines[0].split()))

    def gcd(a, b):

        r = a % b

        if r == 0:
            return int(b)
        
        return gcd(b, r)

    g = gcd(c, d)
    gcm = int(c * d / g)

    c_in = int(b // c - (a-1)//c)
    d_in = int(b // d - (a-1)//d)
    cd_in = int(b // gcm - (a-1)//gcm)

    ans = int((b-a+1) - (c_in + d_in - cd_in))
    print(ans)

main()


