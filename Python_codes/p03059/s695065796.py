a, b, t = [int(x) for x in input().split()]

s = 0
x = a
while x <= t + 0.5:
    s += b
    x += a

print(s)
