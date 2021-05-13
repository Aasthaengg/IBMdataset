n, *a = map(int, open(0).read().split())
print("DENIED" if sum((i % 3) * (i % 5) for i in a if i % 2 == 0) else "APPROVED")