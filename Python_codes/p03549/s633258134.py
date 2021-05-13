a = input().split()
s = int(a[0])
d = int(a[1])
print((1900 * d + 100 * (s - d)) * (2 ** d))