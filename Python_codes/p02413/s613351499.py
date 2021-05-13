r, c = map(int, raw_input().split())
sheet = list()
for i in range(r):
    sheet.append(map(int, raw_input().split()))
for i in range(r):
    sheet[i].append(sum(sheet[i]))
for i in sheet:
    print(" ".join(str(j) for j in i))
temp = list()
for i in range(c):
    result = 0
    for j in range(r):
        result += sheet[j][i]
    temp.append(result)
temp.append(sum(temp))
print(" ".join(str(i) for i in temp))