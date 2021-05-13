a, b, x = map(int, input().split())

if a == 0:
    pa = 0
else:
    pa = (a - 1) // x + 1

if b == 0:
    pb = 1
else:
    pb = b // x + 1

print(pb - pa)


# 0 1 2 3 4 5
# ^
