x,a,b=map(int,input().split())
t=a-b
if t>=0:
    print('delicious')
else:
    if abs(t)<=x:
        print('safe')
    else:
        print('dangerous')
