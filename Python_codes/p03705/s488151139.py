n,a,b=map(int,input().split())
if b<a:
    print(0)
else:
    if n==1 and a!=b:
        print(0)
    else:
        min_=(n-2)*a
        max_=(n-2)*b
        print(max_-min_+1)