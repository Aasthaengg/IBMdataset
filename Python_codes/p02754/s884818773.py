n,a,b=map(int, input().split())

d = a+b
c = n%d
e = n//d

if c <= a:
    print(e*a+c)
if c > a:
    print((e+1)*a)