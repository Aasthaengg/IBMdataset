x,a,b=map(int,input().split())
if a>=b:
    print('delicious')
else:
    if a+x>=b:
        print('safe')
    else:
        print('dangerous')
