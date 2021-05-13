s = input()
n = int(input())
for _ in range(n):
    line = input().split()
    command, args = line[0], line[1:]
    start = int(args[0])
    end = int(args[1]) + 1
    if command == 'replace':
        s = s[:start] + args[2] + s[end:]
    elif command == 'reverse':
        s = s[:start] + str(''.join(list(reversed(s[start:end])))) + s[end:]
    elif command == 'print':
        print(s[start:end])