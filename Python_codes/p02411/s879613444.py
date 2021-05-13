b = []

while True:
    inp = input()
    a = inp.split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    a[2] = int(a[2])
    if a[0] == -1 and a[1] == -1 and a[2] == -1:
        break
    else:
        b.append(a)

for i in b:
    if i[0] == -1 or i[1] == -1:
        print("F")
    elif i[0]+i[1] >= 80:
        print("A")
    elif i[0]+i[1] >= 65:
        print("B")
    elif i[0]+i[1] >= 50:
        print("C")
    elif i[0]+i[1] < 30:
        print("F")
    elif i[2] >= 50:
        print("C")
    else:
        print("D")
