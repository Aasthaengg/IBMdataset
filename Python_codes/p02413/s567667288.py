sheet = []
r, c = (int(x) for x in input().split())

for row in range(r):
    bufarr = [int(x) for x in input().split()]
    bufarr.append(sum(bufarr))
    sheet.append(bufarr)

bufarr = []
for col in range(c + 1):
    bufarr.append(sum(sheet[row][col] for row in range(r)))
sheet.append(bufarr)

for row in range(r + 1):
    print(" ".join(str(sheet[row][col]) for col in range(c + 1)))