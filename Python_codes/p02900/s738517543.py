def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)

def ela(g):
    s={1}
    i=2
    while i*i<=g:
        while g%i==0:
            g//=i
            s.add(i)
        i+=1
    if g!=1: s.add(g)
    return s

a,b=map(int,input().split())
G=gcd(max(a,b),min(a,b))
print(len(ela(G)))