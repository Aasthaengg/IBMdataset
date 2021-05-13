n,k=map(int,input().split())
if k%2:
    print((n//k)**3)
else:
    k//=2
    print((n//k//2)**3+(((n//k)+1)//2)**3)
