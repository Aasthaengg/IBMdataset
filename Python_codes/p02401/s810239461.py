result = []
while True:
    i = input().split()
    if i[1] == '+':
        result = result +[int(i[0]) + int(i[2])]
    elif i[1] == '-':
        result = result + [int(i[0]) - int(i[2])]
    elif i[1] == '/':
        result = result + [int(int(i[0]) / int(i[2]))]
    elif i[1] == '*':
        result = result + [int(i[0]) * int(i[2])]
    elif i[1] == '?':
        break
for i in result:
    print(i)    