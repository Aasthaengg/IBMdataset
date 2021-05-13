W, a, b = map(int, input().split())

xa = abs(a - b-W)
xb = abs(b - a-W)

if (a <= b <=a+W) or (b <= a <= b+W):
    print("0")
else:
    print(min(xa,xb))