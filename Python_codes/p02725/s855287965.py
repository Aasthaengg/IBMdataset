k, n, *a = map(int, open(0).read().split())
a.append(a[0] + k)
print(k - max([abs(a[i + 1] - a[i]) for i in range(n)]))