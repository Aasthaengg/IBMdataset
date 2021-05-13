a=[int(i) for i in input().split()]
print(a[0]+a[1] if a[1]%a[0]==0 else a[1]-a[0])