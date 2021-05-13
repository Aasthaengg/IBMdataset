n,k = map(int,input().split())
if n<k:
    print(0)
elif k==1:
    print(0)
else:
    n-=k
    print(n)