X = int(input())

for a in range(-150, 151):
    for b in range(-150, 151):
        if a ** 5 - b ** 5 == X:
            print(a, b)
            exit()
