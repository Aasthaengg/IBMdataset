def main():

    string = input()
    commands_count = int(input())
    commands = [input().split() for i in range(commands_count)]

    for command in commands:
        a, b = int(command[1]), int(command[2])
        if len(command) == 4:
            string = string[0:a] + command[3] + string[b+1:]
        else:
            if command[0] == 'print':
                print(string[a:b+1])
            else:
                string = string[0:a] + ''.join(list(reversed(string[a:b+1]))) + string[b+1:]

main()