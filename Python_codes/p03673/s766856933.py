n, *a = map(int, open(0).read().split())
print(*(a[::-2] + a[n%2::2]))