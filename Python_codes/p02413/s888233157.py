csum_a = []
r, c = list(map(int, input().split()))
array = [[int(j) for j in input().split()] for i in range(r)]

for i in range(c):
    csum = 0 #列ごとに初期化
    for j in range(r):
        csum = csum + array[j][i]
    csum_a.append(csum)
array.append(csum_a)
#ここの時点で(r+1)行×c列の配列になっている

for i in range((r+1)):
    rsum = 0 #行ごとに初期化
    for j in range(c):
        rsum = rsum + array[i][j]
    array[i].append(rsum)

for i in array:
    print(*i)
