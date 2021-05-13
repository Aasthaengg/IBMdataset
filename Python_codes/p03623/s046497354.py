x,a,b = map(int, input().split())
da = abs(a - x)
db = abs(b - x)
print('A' if da < db else 'B')