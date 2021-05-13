import sys

n = int(input())
for i in range(3500):
    for j in range(3500):
        temp = 4 * (i + 1) * (j + 1) - n * (i + j + 2)
        if temp != 0:
            if (n * (i + 1) * (j + 1)) % temp == 0:
                if (n * (i + 1) * (j + 1)) // temp > 0:
                    print(i + 1, j + 1, (n * (i + 1) * (j + 1)) // temp)
                    sys.exit()