a, b, n = map(int, input().split())

if n < b: x = n
else: x = b - 1

term1 = (a * x) // b
term2 = a * (x // b)

print(term1 - term2)