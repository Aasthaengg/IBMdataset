a, b = map(int, input().split())
n = min(a, b)

m = max(a, b)

if n == 1 and m == 1:
    print(1)
elif n == 1:
    print(m-2)
else:
    print((n-2)*(m-2))
