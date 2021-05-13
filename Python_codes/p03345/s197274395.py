a,b,c,k=map(int,input().split())
if a==b==c:
    print(0)
elif a-b>10**18:
    print('Unfair')
else:
    if k%2==0:
        print(a-b)
    else:
        print(b-a)