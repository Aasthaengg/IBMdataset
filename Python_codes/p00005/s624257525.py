def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)

while 1:
    try:
        a,b=map(int,raw_input().split())
        print gcd(a,b),lcm(a,b)
    except:
        break