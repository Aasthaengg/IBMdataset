a = list(map(int,input().split()))

a.sort()
a.reverse()
print(a[0]*10+a[1]+a[2])