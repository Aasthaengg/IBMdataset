N = int(input())
p = 10**9 + 7

def po(a,n):
    r = 1
    while n != 0:
        if n % 2 == 1:
            r = (r*a)%p
        a = (a*a)%p
        n = n//2
    return r

print((po(10,N)-2*po(9,N)+po(8,N))%p)