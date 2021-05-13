array = []
suum = 0
while True:
    n = int(input())
    if n == 0:
        break
    array.append(n)
for i in range(len(array)):
    for i2 in range(len(str(array[i]))):
        suum += int(str(array[i])[i2])
    print(suum)
    suum = 0