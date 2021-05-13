n = list(map(int, input().split()))

x = n[0]
y = n[1]

if x < y:
    x, y = y, x
while y > 0:
    r = x % y
    x = y
    y = r

print(x)

