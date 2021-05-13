MOD = 10 ** 9
s = int(input())
y = -(-s // MOD)
x = y * MOD - s
print(0, 0, MOD, 1, x, y)