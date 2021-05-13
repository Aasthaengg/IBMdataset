W, a, b = map(int, input().split())

if (a <= b <= a + W) or (a <= b + W <= a + W):
    print(0)
    exit()

if a + W < b:
    print(b - (a + W))
    exit()
else:
    print(a - (b + W))
