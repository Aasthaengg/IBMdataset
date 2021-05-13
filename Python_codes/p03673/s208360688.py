n = int(input())
a = [int(x) for x in input().split()]

if n % 2 == 0:
    b = a[n - 1 : 0 : -2] + a[0 : n - 1 : 2]
else:
    b = a[n - 1 : : -2] + a[1 : n - 1 : 2]

print(*b)