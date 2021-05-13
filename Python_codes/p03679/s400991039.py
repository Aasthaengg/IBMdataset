x, a, b = [int(s) for s in input().split()]
print("delicious" if b <= a else ("safe" if b <= a + x else "dangerous"))