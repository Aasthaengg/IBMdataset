guruguru,line = (input() for i in range(2))
atama = []
target = line[0]
index = -1
saa = True
while True:
    index = guruguru.find(target, index + 1)
    atama.append(index)
    if index == -1:
        break
for i in range(len(atama)):
    stt = ""
    for i2 in range(len(guruguru)):
        if len(guruguru) <= atama[i]+i2:
            index += 1
            stt += guruguru[index]
        else:
            stt += guruguru[atama[i]+i2]
    if line in stt:
        print("Yes")
        saa = False
        break
    index = -1
if saa:
    print("No")