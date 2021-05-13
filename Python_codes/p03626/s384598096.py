import numpy as np
n = int(input())
s1 = list(input())
s2 = list(input())

domino = np.array([s1, s2])
array = []
point = 0
while True:
    col = domino[:, point]
    if col[0] == col[1]:
        array.append(0) # X
        point += 1
    else:
        array.append(1) # Y
        point += 2
    if point >= n:
        break

total = 1
for i in range(len(array)):
    if i == 0:
        if array[i] == 0:
            total *= 3
        else:
            total *= 6
    else:
        if array[i] == 0:
            if array[i-1] == 0:
                total *= 2
            else:
                total *= 1
        else:
            if array[i-1] == 0:
                total *= 2
            else:
                total *= 3
print(total % (10**9 + 7))