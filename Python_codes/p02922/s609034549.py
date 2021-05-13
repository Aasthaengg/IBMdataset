a,b=map(int,input().split())

if b == 1:
    print('0')
elif b <= a :
    print('1')
else:
    b -= a
    a -= 1
    y = b % a
    if y==0:
        print(1 + b//a)
    else:
        print(2 + b//a)

