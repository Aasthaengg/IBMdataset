X = int(input())

loop = True
i = -1

while loop:
    i += 1
    loop = False
    for j in range(2, int(pow(X+i, 1/2)+1)):
        if (X+i) % j == 0:
            loop = True
            break
print(X+i)
