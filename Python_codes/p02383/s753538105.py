a = list(map(int, input().split()))
commands = input()
for command in commands:
    if command == 'N':
        a[0], a[1], a[5], a[4] = a[1], a[5], a[4], a[0]
    elif command == 'S':
        a[0], a[1], a[5], a[4] = a[4], a[0], a[1], a[5]
    elif command == 'W':
        a[0], a[3], a[5], a[2] = a[2], a[0], a[3], a[5]
    elif command == 'E':
        a[0], a[3], a[5], a[2] = a[3], a[5], a[2], a[0]
print(a[0])