n,k = map(int,input().split())

mi = 1
ma = 1 + n-k

if(k==1):
    print(0)
else:
    print(ma-mi)
