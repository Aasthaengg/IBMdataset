def gcd(m,n):  
    while m%n>0:
        m,n=n,m%n
    else:
        return n

while True:
    try:    
        a,b = map(int,raw_input().split())
        a,b = max(a,b),min(a,b)
        g = gcd(a,b)
        l = a*b/g
        print "%d %d" % (g, l)
    except EOFError: 
        break