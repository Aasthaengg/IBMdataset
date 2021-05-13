str = input()
num = int(input())
for i in range(num):
    command = input().split()
    c1, c2, c3 = command[0], int(command[1]), int(command[2])
    if c1 == 'print':
        print(str[c2:c3 + 1])
    elif c1 == 'reverse':
        str = str[:c2] + str[c2:c3 + 1][::-1] + str[c3 + 1:]
    elif c1 == 'replace':
        str = str[:c2] + command[3] + str[c3 + 1:]