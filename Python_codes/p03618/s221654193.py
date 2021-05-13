s = input()
x = 1
d = {}
for i, c in enumerate(s):
    k = d.get(c, 0)
    d[c] = k + 1
    x += (i - k)
print(x)
