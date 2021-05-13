a, b, c, d = map(int, input().split())
t = (c + b - 1) // b
a = (a + d - 1) // d
print('Yes' if t <= a else 'No')
