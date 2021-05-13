iranai = [int(i) for i in input().split()]
iru = [[int(i) for i in input().split()] for i in range(iranai[0])]
mikitani = []
son = []
num = 0
mikicount = 0
for i in range(iranai[0]):
    for i2 in range(iranai[1]):
        num += iru[i][i2]
    mikitani.append(num)
    num = 0

for i in range(iranai[1]):
    for i2 in range(iranai[0]):
        num += iru[i2][i]
    son.append(num)
    num = 0

for i in range(iranai[0]):
    for i2 in range(iranai[1]):
        print(iru[i][i2],end=" ")
        if i2 == iranai[1]-1:
            print(mikitani[i])
    mikicount += mikitani[i]
son.append(mikicount)

for i in range(len(son)):
    if i == len(son)-1:
        print(son[i])
    else:
        print(son[i],end=" ")