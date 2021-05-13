a = list(map(int, input().split()))
for i in range(a[2]):
    a[i%2] -= a[i%2]%2
    a[i%2] //= 2
    a[1-i%2] += a[i%2]
print(a[0],a[1])