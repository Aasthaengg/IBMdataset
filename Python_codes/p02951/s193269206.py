a=list(map(int,input().split()))
if a[0]<=a[1]+a[2]:
    print(a[2]+a[1]-a[0])
else:
    print('0')