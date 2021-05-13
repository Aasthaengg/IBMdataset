Sa = input()
Sb = input()
Sc = input()
data = [Sa, Sb, Sc]
target = 0
while True:
    if(data[target] == ""):
        if target == 0:
            print("A")
        if target == 1:
            print("B")
        if target == 2:
            print("C")
        break
    if data[target][0] == "a":
        data[target] = data[target][1:]
        target = 0
    elif data[target][0] == "b":
        data[target] = data[target][1:]
        target = 1
    elif data[target][0] == "c":
        data[target] = data[target][1:]
        target = 2