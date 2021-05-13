n, a, b = map(int, input().strip().split(" "))

win = "Borys"
if abs(a-b) % 2 == 0:
    win = "Alice"

print(win)