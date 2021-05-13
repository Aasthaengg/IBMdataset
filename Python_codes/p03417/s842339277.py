#090_C
n,m=map(int,input().split())
if n>1 and m>1:
    print((n-2)*(m-2))
else:
    print(max(1,n-2)*max(1,m-2))