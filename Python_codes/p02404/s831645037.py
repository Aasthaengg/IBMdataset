h = 0
w = 0
dataset = []

while True:
    h, w = map(int, input().split())
    if (h >= 3 and h <= 300) and (w >= 3 and w <= 300):
        listed = []
        listed.append(h)
        listed.append(w)
        dataset.append(listed)
    elif h == 0 and w == 0:
        break
    else:
        break

for listed in dataset:
    h = listed[0]
    w = listed[1]

    for i in range(0, 1):
        for j in range(w):
            print("#", end="")
        print()
    for i in range(1, h-1):
        for j in range(0, 1):
            print("#", end="")
        for j in range(1, w-1):
            print(".", end="")
        for j in range(w-1, w):
            print("#", end="")
        print()
    for i in range(h-1, h):
        for j in range(w):
            print("#", end="")
        print()
    print()