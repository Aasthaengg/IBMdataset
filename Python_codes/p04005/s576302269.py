a = list(map(int,input().split()))
if a[0] % 2 == 0 or a[1] % 2 == 0 or a[2] % 2 == 0:
    print(0)
else:
    print(min(a[0]*a[1],a[1]*a[2],a[0]*a[2]))