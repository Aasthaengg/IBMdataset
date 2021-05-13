
a,b = map(int, input().split())
c=str(a)*b
d=str(b)*a

if c>d:
    print(d)
else:
    print(c)
