a = [int(_) for _ in input().split()]
a.sort()
print(a[1]-a[0]+a[2]-a[1])