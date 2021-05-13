p = list(map(int, input().split()))
n = p[0]
a = p[1]
b = p[2]

if a*n >= b:
    print(b)
else:
    print(a*n)