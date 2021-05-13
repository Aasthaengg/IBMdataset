import fractions

n,*t=map(int,open(0).read().split())

if n==1:
    print(t[0])
else:
    g=fractions.gcd(t[0],t[1])
    l=t[0]*t[1]//g

    for i in range(2,n):
        l=t[i]*l//fractions.gcd(l,t[i])
        g=fractions.gcd(l,t[i])

    print(l)