a, b = (int(n) for n in input().split())
if a <= b: print(str(a) * b)
else: print(str(b) * a)