def gcd(m,n):
    if  m%n == 0:
        return n
    return gcd(n,m%n)

a,b,c = map(int,input().split())
if c%gcd(a,b)==0:
    print("YES")
else:
    print("NO")