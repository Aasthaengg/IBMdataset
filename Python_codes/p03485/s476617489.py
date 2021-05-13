a, b = map(int, (input().split()))

c = (a + b) // 2
d = (a + b) % 2

if d != 0:
    print(c + 1)
else:
    print(c)
