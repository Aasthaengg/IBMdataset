a,b,n=list(map(int,input().split()))
if b==1:
    print(0)
elif n>=b:
    k=n%b
    if k==b-1:
        print(int(a*(n)/b)-a*int(n/b))
    else:
        print(int(a*(n-k-1)/b)-a*int(n/b-1))
else:
    print(int(a*n/b))