
a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
if a>b:
    x=a-v*t
    y=b-w*t
    if x<=y:
        print('YES')
    else:
        print('NO')
else:
    x=a+v*t
    y=b+w*t
    if x>=y:
        print('YES')
    else:
        print('NO')