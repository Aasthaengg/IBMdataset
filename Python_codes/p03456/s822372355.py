a,b=input().split()

c=int(a+b)

if (c**0.5) % int(c**0.5) ==0:
    print('Yes')
else:
    print('No')