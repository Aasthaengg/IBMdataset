X = int(input())

for i in range(-700, 701):
    for j in range(-700, 701):
        if i ** 5 - j ** 5 == X:
            print(i, j)
            exit()