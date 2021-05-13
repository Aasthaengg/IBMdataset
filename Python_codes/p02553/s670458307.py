a, b, c, d = map(int, open(0).read().split())
print(max(a*c,a*d,b*c,b*d))