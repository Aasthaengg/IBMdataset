# ABC 063: A – Restricted
a, b = [int(s) for s in input().split()]
print(a + b if a + b < 10 else 'error')