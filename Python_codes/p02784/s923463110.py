h,n=map(int,input().split())
a=list(map(int, input().strip().split()))[:n]
b=sum(a)
if (b>=h):
    print('Yes')
else:
    print("No")
