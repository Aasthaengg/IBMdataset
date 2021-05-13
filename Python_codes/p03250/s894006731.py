a = [int(x) for x in input().split()]
a.sort(reverse=True)
print(10 * a[0] + a[1] + a[2])
