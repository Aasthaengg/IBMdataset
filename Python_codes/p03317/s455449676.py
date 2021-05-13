n, k = map(int, input().split())
m = n - 1
l = k - 1

if m % l == 0:
    print(m // l)
else:
    print(m // l + 1)