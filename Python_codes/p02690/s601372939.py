
X = int(input())
flag = True
for a in range(-200, 200):
    for b in range(-200, 200):
        if a ** 5 - b ** 5 == X and flag:
            print(a, b)
            flag = False

