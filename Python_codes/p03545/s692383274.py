from itertools import product

a, b, c, d = [int(i) for i in list(input())]
for i, j in zip(product([1, -1], repeat=3), product(["+", "-"], repeat=3)):
    if a + b * i[0] + c * i[1] + d * i[2] == 7:
        print(f"{a}{j[0]}{b}{j[1]}{c}{j[2]}{d}=7")
        break