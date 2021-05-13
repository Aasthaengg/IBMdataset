a = list(map(int,input().split()))
a.sort()
if (a[2]-a[1])%2==0 and (a[2]-a[0])%2==0:
    print((a[2]-a[1])//2+(a[2]-a[0])//2)
elif (a[2]-a[1])%2==1 and (a[2]-a[0])%2==1:
    print((a[2]-a[1])//2+(a[2]-a[0])//2+1)
else:
    print((a[2]-a[1])//2+(a[2]-a[0])//2+2)