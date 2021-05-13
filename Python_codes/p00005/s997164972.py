import sys

for i in sys.stdin:
    a,b=list(map(int, i.split()))
    d=a*b
    if a>b:
        temp=a
        a=b
        b=temp
    c=a%b
    while c!=0:
        a=b
        b=c
        c=a%b
    g=b
    l=int(d/g)
    print("{} {}".format(g,l))