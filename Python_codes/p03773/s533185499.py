# ABC 057: A – Remaining Time
a, b = [int(s) for s in input().split()]
print(a + b if a + b <= 23 else a + b - 24)