N, *A = map(int, open(0).read().split())
print("first") if any(a % 2 for a in A) else print("second")
