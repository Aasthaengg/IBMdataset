import fractions

n,m=list(map(int,input().split()))
s=input()
t=input()
l=n*m//fractions.gcd(n,m)

m,n=(m//fractions.gcd(m,n),n//fractions.gcd(m,n))
p=m*n//fractions.gcd(m,n)

pos=0
while pos<l:
    if s[pos//m]!=t[pos//n]:
        print(-1)
        exit(0)

    pos+=p

print(l)