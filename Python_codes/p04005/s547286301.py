a = list(map(int,input().split()))
a.sort(reverse = True)
block = a[0] * a[1] * a[2]
a[0] = a[0] // 2
x = a[0] * a[1] * a[2]
y = block - x
print(abs(x - y))