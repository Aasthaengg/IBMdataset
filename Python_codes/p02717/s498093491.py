a = [int(i) for i in input().split()]
a[0],a[1] = a[1],a[0]
a[0],a[2] = a[2],a[0]
print(" ".join(map(str,a)))
