X, Y = map(int, input().split())

max_Y = 4 * X
min_Y = 2 * X
if max_Y < Y:
    print("No")
    exit()

y = max_Y
while y >= min_Y:
    if y == Y:
        print("Yes")
        exit()
    else:
        y -= 2
print("No")
