x = int(input())
print(max(b**p if b**p <= x else 0 for b in range(1, 35) for p in range(2, 10)))