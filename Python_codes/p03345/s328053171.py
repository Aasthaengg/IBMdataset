a,b,c,k= map(int,input().split())
s = a+b+c
ans = a - b

    
if ((-1)**k)*(a-b) <= 10 **18:
    print(((-1)**k)*(a-b) )
else:
    print('Unfair')