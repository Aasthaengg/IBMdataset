N = int(input())
SP = []
for i in range(N):
    line = input().split()
    s = line[0]
    p = int(line[1])
    # レストラン番号と紐付けておく
    SP.append([s, p, i + 1])
# SPの中身はそれぞれ[市名, 点数, 店番号]
# 市名で昇順ソート、更に点数で降順ソート
SP = sorted(SP, key=lambda x: (x[0], -x[1]))
for spi in SP:
    print(spi[2])
