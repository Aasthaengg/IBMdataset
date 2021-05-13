while True:
    a = input()
    if '?' in a:
        break
    print("{0}".format(eval(a.replace('/', '//'))))