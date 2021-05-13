a = list(map(int, input().split()))

print(a[0]+a[1] if a[0]+a[1] < 24 else a[0]+a[1]-24)