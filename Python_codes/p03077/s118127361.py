n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

m = min([a, b, c, d, e])

if n % m == 0:
    print(n//m + 4)
else:
    print(n//m + 4 + 1)