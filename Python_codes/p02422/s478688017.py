def do_transform(txt, *args):
    op = args[0]
    a = int(args[1])
    b = int(args[2])
    if op == 'print':
        print(txt[a:b+1])
        return txt
    elif op == 'reverse':
        first_part = txt[:a]
        second_part = txt[a:b+1]
        third_part = txt[b+1:]
        return first_part + second_part[::-1] + third_part
    elif op == 'replace':
        p = args[3]
        first_part = txt[:a]
        third_part = txt[b+1:]
        return first_part + p + third_part


if __name__ == '__main__':
    # ??????????????\???
    text = input()
    op_count = int(input())
    transformations = []
    for i in range(op_count):
        data = [x for x in input().split(' ')]
        transformations.append(data)

    # ???????????????
    for d in transformations:
        text = do_transform(text, *d)
        # print('debug: {0}'.format(text))

    # ???????????????