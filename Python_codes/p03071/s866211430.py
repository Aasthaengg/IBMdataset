a, b = map(int, input().split())
if a > b: print(a + (a - 1))
if b > a: print(b + (b - 1))
if b == a: print(a + b)