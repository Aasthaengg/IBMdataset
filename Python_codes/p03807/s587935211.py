N, *A = map(int, open(0).read().split())
print("YNEOS"[sum(a&1 for a in A)&1::2])