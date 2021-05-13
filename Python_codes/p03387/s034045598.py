a = list(map(int,input().split()))
a.sort()
if (a[1]-a[0]) % 2 == 0:
    print((a[1]-a[0])//2 + (a[2]-a[1]))
else:
    print((a[2]-a[1])//2 + (a[2]-a[1])%2 + (a[2]-a[0]+1)//2 + 1)    