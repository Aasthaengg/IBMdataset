n, *dd = map(int, open(0).read().split())

dd.sort()

print(dd[n//2] - dd[n//2-1])