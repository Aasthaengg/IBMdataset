n, *a = map(int, open(0).read().split())
print(sum(a[b - 1] == e + 1 for e, b in enumerate(a)) // 2)