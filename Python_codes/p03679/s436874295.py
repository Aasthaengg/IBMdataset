def resolve():
    x,a,b=map(int, input().split())
    if b-a>=x+1:
        print('dangerous')
    elif b-a<=0:
        print('delicious')
    else:
        print('safe')
resolve()