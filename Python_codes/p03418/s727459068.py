n,k=map(int,input().split())
if k==0:
    print(n*n)
else:
    a=0
    for b in range(n+1):
        if k<b:a+=n//b*(b-k)+max(0,n-n//b*b-k+1)
    print(a)