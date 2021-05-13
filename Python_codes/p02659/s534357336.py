# coding: utf-8
# Your code here!

a,b=input().split()
b=list(b)
if a=="0" or b=="0":
    print(0)
else:
    b.remove('.')
    b=''.join(b)
    a=int(a)
    b=int(b)
    c=str(a*b)
    if a*b<100:
        print(0)
    else:
        c=list(c)
        del c[-1]
        del c[-1]
        c=''.join(c)
        print(c)
