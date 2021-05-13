x,a,b=map(int,input().split())
if b-a<=x:
    if b-a<=0:
        print('delicious')
    else:
        print('safe')
else:
    print('dangerous')