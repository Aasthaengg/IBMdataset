size = list(map(int, input().split()))
sheet = []

for i in range(size[0]):
    value = list(map(int, input().split()))
    sheet.extend(value)
    sheet.append(sum(value))

for i in range(size[1]+1):
    
    point = i
    vsum = 0
    
    for j in range(size[0]):
        vsum += sheet[point]
        point += size[1] +1
    sheet.append(vsum)
    
for i in range(len(sheet)):
    if (i+1) % (size[1]+1)  == 0:
        print(sheet[i])
    else:
        print(str(sheet[i])+" ", end="")