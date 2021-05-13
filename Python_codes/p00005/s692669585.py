import math
while True:
    try :
        a,b = map(int,input().split())
        gcd = math.gcd(a,b)
        c= a/gcd
        d= b/gcd
        print(gcd,int(c*d*gcd))
    except EOFError:
        break
