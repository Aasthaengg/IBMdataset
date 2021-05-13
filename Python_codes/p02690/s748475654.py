
X = int(input())
flag = False
for a in range(-200, 200):
    for b in range(-200, 200):
        if a ** 5 - b ** 5 == X:
            print(a, b)
            flag = True
            break

    if flag:
        break
