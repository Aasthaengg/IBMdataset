n, *a = map(int, open(0).read().split())
print("YNEOS"[sum(a)%2::2])