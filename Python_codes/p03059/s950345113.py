a, b, t = map(int, input().split())
c = 0
while t >= a:
    t -= a
    c += 1
print(b * c)