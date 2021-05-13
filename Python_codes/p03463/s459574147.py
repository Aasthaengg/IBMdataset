n,a,b=map(int,input().split())
if n==2:
    print('Borys')
else:
    if (b-a)%2==0:
        print('Alice')
    elif n%2==0 and (b-a)%2==0:
        print('Draw')
    else:
        print('Borys')
