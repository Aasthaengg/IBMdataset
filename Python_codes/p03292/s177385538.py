a = list(map(int, input().split()))

a1 = abs(a[0] - a[1])
a2 = abs(a[1] - a[2])
a3 = abs(a[2] - a[0])

m = max(a1, a2, a3)
#print(m)
print(a1 + a2 + a3 - m)