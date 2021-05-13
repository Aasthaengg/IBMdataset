def calc_gcd(a,b):
    if a < b:
        a,b=b,a
    if b == 0:
        return a
    return calc_gcd(b,a%b)

x,y=map(int,input().split())
print("%d"%(calc_gcd(x,y)))

