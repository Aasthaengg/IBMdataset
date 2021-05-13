n, l = list(map(int, input().split()))

c = ((l) + (l+n-1)) * n // 2

if 0 < l:
    c -= l
elif l <= 0 <= l + n - 1:
    pass
else:
    c -= (l+n-1)

print(c)