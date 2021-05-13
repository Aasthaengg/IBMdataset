a,b,c,n = map(int, input().split())

ans = (-1)**n*a+(-1)**(n-1)*b

if abs(ans)>10**18:
    print('Unfair')
else:
    print(int(ans))
