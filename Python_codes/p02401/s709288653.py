while True:
    try:
        buf = input()
        print(int(eval(buf)))
    except:
        a, op, b = buf.split(' ')
        if op == '?':
            exit()