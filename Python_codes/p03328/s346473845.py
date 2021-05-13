a, b = map(int, input().split())
c = b - a
d = 0
for i in range(c, 0, -1):
    d += i
print(d - b)