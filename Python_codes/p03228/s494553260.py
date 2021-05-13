def resolve():
    a,b,k=map(int,input().split())
    while 1:
        if a%2==1:
            a-=1
        a//=2
        b+=a
        k-=1
        if k==0:
            break
        if b%2==1:
            b-=1
        b//=2
        a+=b
        k-=1
        if k==0:
            break
    print('{} {}'.format(a,b))
resolve()