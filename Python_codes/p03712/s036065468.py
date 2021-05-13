import numpy as np

H, W = (int(x) for x in input().split())

a = []
for i in range(H):
    a.append(input())

for i in range(0, H + 2):
    for j in range(0, W + 2):
        if (i == 0) | (j == 0) | (i == (H + 1)) | (j == (W + 1)):
            print("#", end='')
        elif j == 1:
            print(a[i - 1], end='')

        if j == (W + 1):
            print("")
