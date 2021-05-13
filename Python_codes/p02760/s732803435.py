import numpy as np

bingo = []
for _ in range(3):
    array = list(map(int,input().split()))
    bingo.append(array)
bingo = np.array(bingo)
n = int(input())
bs = []
for _ in range(n):
    bs.append(int(input()))

for i in bs:
    bingo = np.where(bingo == i, 101, bingo)

h = False
if bingo[0][0] == bingo[1][1] == bingo[2][2] or bingo[0][2] == bingo[1][1] == bingo[2][0]:
    h = True
if h == False:
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2]:
            h = True
            break
    for j in range(3):
        if bingo[0][j] == bingo[1][j] == bingo[2][j]:
            h = True
            break

print('Yes') if h == True else print('No')