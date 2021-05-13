array = []
while True:
    n =input()
    if n == "-1 -1 -1":
        break
    array.append(n.split())
suum = 0
seiseki = []
for i in range(len(array)):
    if array[i][0]!="-1" and array[i][1] != "-1":
        suum = int(array[i][0]) + int(array[i][1])
        if suum >= 80:
            seiseki.append("A")
        elif suum < 80 and suum >= 65:
            seiseki.append("B")
        elif suum < 65 and suum >= 50:
            seiseki.append("C")
        elif suum <50 and suum >= 30:
            if int(array[i][2]) >= 50:
                seiseki.append("C")
            else:
                seiseki.append("D")
        else:
            seiseki.append("F")
    else:
        seiseki.append("F")
    print(seiseki[i])