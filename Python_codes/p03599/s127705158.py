a,b,c,d,e,f = map(int, input().strip().split(" "))
a = 100 * a
b = 100 * b
e = e * 100 / (100.0+e)

water = set([])
for i in range((f+a)//a):
    for j in range((f+b)//b):
        w = a * i + b * j
        if w <= f and 0 < w:
            water.add(a * i + b * j)


sugar = set([])
for i in range((f+c)//c):
    for j in range((f+d)//d):
        s = c * i + d * j
        if s <= f:
            sugar.add(c * i + d * j)
density = -1
_s = 0
sw = 0
for w in water:
    for s in sugar:
        _d = 100 * s / (s+w)
        if _d <= e and w + s <= f and density < _d:
            density = _d
            sw = w + s
            _s = s

print(sw, _s)
