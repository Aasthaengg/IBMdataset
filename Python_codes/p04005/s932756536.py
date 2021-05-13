a = list(map(int,input().split()))
a.sort(reverse = True)
if a[0] % 2 == 0 or a[1] % 2 == 0 or a[2] % 2 == 0:
    print(0)
    exit(0)
block = a[0] * a[1] * a[2]
a[0] = a[0] // 2
x = a[0] * a[1] * a[2]
y = block - x
print(abs(x - y))