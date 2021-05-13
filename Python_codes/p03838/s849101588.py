import sys
a,b = map(int,input().split())
if a*(-1) == b:
    print(1)
    sys.exit()
if a*b > 0:
    if a >0:
        if a < b:
            #
            print(b-a)
        else:
            #
            print(a-b+2)
    else:
        if a < b:
            #
            print(b-a)
        else:
            #
            print(-b+a+2)
elif a*b < 0:
    if a < 0:
        if abs(a)>abs(b):
            #
            print(-b-a+1)
        else:
            #
            print(b+a+1)
    else:
        if abs(a)>abs(b):
            #
            print(b+a+1)
        else:
            #
            print(-b-a+1)
else:
    if a == 0:
        if b > 0:
            print(b)
        else:
            print(-b+1)
    else:
        if a > 0:
            print(a+1)
        else:
            print(-a)