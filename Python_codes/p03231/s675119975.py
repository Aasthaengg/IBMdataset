def gcd(m,n):
    while (m % n != 0):
        n,m = m%n,n
    return(n)

def lcm(m,n):
    return(m * n // gcd(m,n))

n,m = map(int,input().split())

s = input()
t = input()


g = gcd(m,n)

if(g in [n,m]):
    print(-1)
else:
    x = lcm(m,n)
    a = x // n
    b = x // m
    for i in range(n//b):
        ai = b * i
        bi = a * i
        if(s[ai] != t[bi]):
            print(-1)
            exit()
    print(lcm(m,n))