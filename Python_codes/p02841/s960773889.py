def resolve():
    m1,d1=map(int, input().split())
    m2,d2=map(int, input().split())
    if m2==m1+1 and d2==1:
        print('1')
    elif m1==12 and m2==1 and d2==1:
        print('1')
    else:
        print('0')
resolve()