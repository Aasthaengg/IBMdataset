a = list(map(int,input().split()))
if a[2]-(a[0]-a[1]) < 0:
    print(0)
else:
    print(a[2]-(a[0]-a[1]))