opArray = []
answers = []

a, op, b = input().split()

while op != '?':
    opArray.append([a, op, b])
    a, op, b = input().split()

for i in range(len(opArray)):
    if opArray[i][1] == "+":
        answers.append(int(opArray[i][0]) + int(opArray[i][2]))
    elif opArray[i][1] == "-":
        answers.append(int(opArray[i][0]) - int(opArray[i][2]))
    elif opArray[i][1] == "/":
        answers.append(int(int(opArray[i][0]) / int(opArray[i][2])))
    elif opArray[i][1] == "*":
        answers.append(int(opArray[i][0]) * int(opArray[i][2]))
    else:
        break

for i in answers:
    print(i)