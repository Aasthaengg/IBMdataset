x,a,b= list(map(int, input().split()))
if a>=b:
    print('delicious')
else:
    n=b-a
    if n<=x:
        print('safe')
    else:
        print('dangerous')