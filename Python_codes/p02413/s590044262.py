n, m = map(int, input().split())
matrix = list()
for i in range(n):
    hoge = list()
    for elem in map(int, input().split()):
        hoge.append(elem)
    hoge.append(sum(hoge))
    matrix.append(hoge)
last_raw = list()
for j in range(m+1):
    hoge = 0
    for i in range(n):
        hoge += matrix[i][j]
    last_raw.append(hoge)
matrix.append(last_raw)
for i in range(n+1):
    print (' '.join(map(str, matrix[i])))
