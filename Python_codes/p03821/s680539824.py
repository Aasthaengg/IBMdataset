(n, ), *s = [[*map(int, i.split())] for i in open(0)]
c = 0
for a, b in reversed(s):
    q = (a + c) % b
    c += b * (q > 0) - q
print(c)
