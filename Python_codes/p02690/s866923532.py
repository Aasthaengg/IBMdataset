import math
X = int(input())

## 全探索
for i in range(-200, 200):
    for j in range(-200, 200):
        if i**5 - j**5 == X:
            print("{} {}".format(i, j))
            exit()
