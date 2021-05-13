str = input()
for q in range(int(input())):
    com, *num = input().strip().split()
    a, b = int(num[0]), int(num[1])
    if com == 'print':
        print(str[a:b+1])
    elif com == 'replace':
        if b == len(str)-1:
            str = str[:a] + num[2]
        else:
            str = str[:a] + num[2] + (str[b+1:])
    else: # com == 'reverse'
        if a == 0:
            str = str[b::-1] + str[b+1:]
        elif b == len(str)-1:
            str = str[:a] + str[:a-1:-1]
        else:
            str = str[:a] + str[b:a-1:-1] + str[b+1:]