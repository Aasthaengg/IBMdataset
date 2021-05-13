h, w = [int(x) for x in input().split()]
c = "#"
s = c * (w + 2)
print(s)
for _ in range(h):
    print(c + input() + c)
print(s)