n,k=map(int,input().split())
if n%2==1:
    if k<=n//2+1:
        print('YES')
    else:
        print('NO')
else:
    if k<=n//2:
        print('YES')
    else:
        print('NO')
