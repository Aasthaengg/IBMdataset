c = [input().split() for _ in range(3)]

for a1 in range(101):
    b1 = int(c[0][0]) - a1
    if b1 < 0:
        continue

    b2 = int(c[0][1]) - a1
    if b2 < 0:
        continue

    b3 = int(c[0][2]) - a1
    if b3 < 0:
        continue

    a2 = int(c[1][0]) - b1
    if a2 < 0:
        continue

    a3 = int(c[2][0]) - b1
    if a3 < 0:
        continue

    if int(c[1][1]) != (a2 + b2):
        continue

    if int(c[1][2]) != (a2 + b3):
        continue

    if int(c[2][1]) != (a3 + b2):
        continue

    if int(c[2][2]) != (a3 + b3):
        continue

    print("Yes")
    break

else:
    print("No")