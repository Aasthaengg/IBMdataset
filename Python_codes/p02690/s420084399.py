X = int(input())

for a in range(121):
    for b in range(121):
        if a ** 5 - b ** 5 == X:
            print(a, b)
            break
        elif a ** 5 + b ** 5 == X:
            print(a, -b)
            break
    else:
        continue
    break
