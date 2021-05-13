def transformate(s, command):
    command, *op = command.split()

    op[0] = int(op[0])
    op[1] = int(op[1])

    if command == 'replace':
        return s[0:op[0]] + op[2] + s[op[1]+1:]
    elif command == 'reverse':
        return s[0:op[0]] + s[op[0]:op[1]+1][::-1] + s[op[1]+1:]
    elif command == 'print':
        print(s[op[0]:op[1]+1])
        return s

if __name__ == '__main__':
    s = input()
    for _ in range(int(input())):
        s = transformate(s, input())

