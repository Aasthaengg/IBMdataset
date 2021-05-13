a,b,c=map(int,input().split())
if b>=a*c:
    print(c)
elif b>=a:
    print(b//a)
else:
    print('0')
