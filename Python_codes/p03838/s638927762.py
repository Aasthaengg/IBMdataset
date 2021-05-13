x, y = map(int, input().split())
if x <= y:
    print(min(y - x, abs(y + x) + 1))
else:
    print(min(abs(y + x) + 1, abs(y - x) + 2))
