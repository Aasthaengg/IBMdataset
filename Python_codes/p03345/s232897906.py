a, b, c, k = [int(i) for i in input().split()]
if abs(a - b) > 10 ** 18:
    print("Unfair")
else: print(a - b if k % 2 == 0 else b - a)