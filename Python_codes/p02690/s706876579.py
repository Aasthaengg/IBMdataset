X = int(input())
A = 0
B = 0
for i in range(-200, 201):
    for j in range(-200, 201):
        if i ** 5 - j ** 5 == X:
            A, B = i, j
            break

print(A, B)
