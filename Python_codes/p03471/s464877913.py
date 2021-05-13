n, Y = map(int, input().split())
frag = 0
tmp = 0
a = 0
b = 0
c = 0
for x in range(n + 1):
    for y in range(n - x + 1):
        tmp = x * 10000 + y * 5000 + (n - x - y) * 1000
        if tmp == Y:
            frag = 1
            a = x
            b = y
            c = n - x - y
            break
if frag == 0:
    print("-1 -1 -1")
else:
    print(f"{a} {b} {c}")
