x, y = map(int, input().split())
s = [300000, 200000, 100000] + [0] * 500
z = s[x - 1] + s[y - 1] + (400000 if x == 1 and y == 1 else 0)
print(z)