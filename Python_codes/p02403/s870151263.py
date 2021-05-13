h = 0
w = 0
dataset = []

while True:
    h, w = map(int, input().split())
    if (h > 0 and h <= 300) and (w > 0 and w <= 300):
        listed = []
        listed.append(h)
        listed.append(w)
        dataset.append(listed)
    else:
        break

for listed in dataset:
    h = listed[0]
    w = listed[1]

    for i in range(h):
        for j in range(w):
            print("#", end="")
        print()
    print()