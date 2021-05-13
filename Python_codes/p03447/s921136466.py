a = [int(input()) for _ in range(3)]
a[0] -= a[1]
print(a[0]-(a[0]//a[2])*a[2])
