a, b, c, k = [int(w) for w in input().split()]

print(a - b if k % 2 == 0 else b - a)
