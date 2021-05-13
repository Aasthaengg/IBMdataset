r, c = map(int, input().split())
a = [[0 for i in range(c+1)] for j in range(r+1)]

###### 入力データの代入 ######
for i in range(r):
    for j, x in enumerate(input().split()):
        a[i][j] = int(x)

###### 各行の合計を求める ######
for i, line in enumerate(a):
    a[i][c] = sum(line)

###### 行と列を入れ替える ######
a = list(zip(*a))

###### 各列の合計を求める ######
for i, line in enumerate(a):
    a[i] = list(line)
    a[i][r] = sum(a[i])

###### 行と列を入れ替える ######
a = list(zip(*a))

for line in a:
    for i, x in enumerate(line):
        if i == c:
            print(x)
        else:
            print(x, end=" ")

