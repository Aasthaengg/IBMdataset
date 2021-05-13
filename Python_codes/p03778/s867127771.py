W, a, b = map(int, input().split())
if a + W >= b:
    if b + W < a:
        print(a - b -W)
    else:
        print(0)
else:
    print(b - a - W)
