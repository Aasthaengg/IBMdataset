N, *L = map(int, open(0).read().split())
L.sort()
print("Yes") if sum(L[:-1]) > L[-1] else print("No")
