n, *a = map(int, open(0).read().split())
a = sorted(a)[::-1]
print(sum(a[0::2]) - sum(a[1::2]))
