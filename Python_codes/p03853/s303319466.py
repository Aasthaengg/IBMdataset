# coding = SJIS

h, w = map(int, input().split())
row = []

for i in range(h):
    row.append(str(input()))

for i in range(h):
    for j in range(2):
        print(row[i])
