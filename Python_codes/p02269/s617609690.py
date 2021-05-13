def use_dictionary(commands):
    d = {}
    for cmd, word in commands:
        if cmd == 'insert':
            d[word] = True
        elif cmd == 'find':
            if word in d:
                print('yes')
            else:
                print('no')

if __name__ == '__main__':
    # ??????????????\???
    commands = []
    # commands.append(('insert', 'AAA'))
    # commands.append(('insert', 'AAC'))
    # commands.append(('find', 'AAA'))
    # commands.append(('find', 'CCC'))
    # commands.append(('insert', 'CCC'))
    # commands.append(('find', 'CCC'))
    num = int(input())
    for i in range(num):
        commands.append([x for x in input().split(' ')])

    # ???????????????
    use_dictionary(commands)

    # ???????????¨???