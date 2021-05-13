W = input()

c = 0
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    for w in line.lower().split():
        if w == W:
            c += 1
print(c)

