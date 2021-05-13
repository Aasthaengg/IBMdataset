x,y = map(int,input().split())
a = 300000
b = 200000
c = 100000

if x == 1:
    if y==1:
        print(1000000)
    elif y==2:
        print(a+b)
    elif y==3:
        print(a+c)
    else:
        print(a)
if x == 2:
    if y==1:
        print(a+b)
    elif y==2:
        print(b+b)
    elif y==3:
        print(b+c)
    else:
        print(b)
if x == 3:
    if y==1:
        print(a+c)
    elif y==2:
        print(c+b)
    elif y==3:
        print(c+c)
    else:
        print(c)
if x>3 and y>3:
    print(0)
if x>3 and y == 1:
    print(a)
if x>3 and y == 2:
    print(b)
if x>3 and y == 3:
    print(c)
