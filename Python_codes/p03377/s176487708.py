A,B,X=map(int,input().split())
if A<=X:
    if B>=X-A:
        print('YES')
    else:
        print('NO')
else:
    print('NO')