read = lambda: list(map(int, input().split()))
w, h, x, y = read()
sq = w * h / 2
if w == x * 2 and h == y * 2:
    print(sq, 1)
else:
    print(sq, 0)