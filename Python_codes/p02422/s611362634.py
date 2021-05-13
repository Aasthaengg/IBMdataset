s = input()
for _ in [0]*int(input()):
    command = []
    command.append(list(map(str,input().split())))
   # print(command[0][0])
    if command[0][0] == 'replace':
        s = s[:int(command[0][1])] + command[0][3] + s[int(command[0][2])+1:]
    elif command[0][0] == 'reverse':
        temp =  s[int(command[0][1]):int(command[0][2])+1:]
        s = s[:int(command[0][1])] +temp[::-1] + s[int(command[0][2])+1:]
    elif command[0][0] == 'print':
        print(s[int(command[0][1]):int(command[0][2])+1])

