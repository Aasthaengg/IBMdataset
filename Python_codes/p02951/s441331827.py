a,b,c = map(int,input().split())

a -= b

c -= a

if(c >= 0):
    print(c)
else:
    print(0)
