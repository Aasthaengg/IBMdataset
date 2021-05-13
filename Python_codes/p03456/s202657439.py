a,b=map(str,input().split())
c=a+b
c=(int(c)**(1/2))
if (c.is_integer())==True:
    print('Yes')
else:
    print('No')