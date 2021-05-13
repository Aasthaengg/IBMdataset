w, a, b = [int(x) for x in input().split()]
if abs(a - b) <= w:
    res = 0
else:
    res = min(abs(a + w - b), abs(b + w - a))
print(res)
