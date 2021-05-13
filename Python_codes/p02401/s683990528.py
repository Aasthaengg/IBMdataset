import math
ops = []
kekka = []

while True:
    op = [e for e in input().split()]
    if op[1]=="?":
        break
    ops.append(op)

for i in range(len(ops)):
    if ops[i][1]=="+":
        sum = int(ops[i][0]) + int(ops[i][2])
        kekka.append(sum)
    elif ops[i][1]=="-":
        hiku = int(ops[i][0]) - int(ops[i][2])
        kekka.append(hiku)
    elif ops[i][1]=="*":
        kakeru = int(ops[i][0]) * int(ops[i][2])
        kekka.append(kakeru)
    elif ops[i][1]=="/":
        waru = math.floor(int(ops[i][0]) / int(ops[i][2]))
        kekka.append(waru)

for j in kekka:
    print(int(j))
