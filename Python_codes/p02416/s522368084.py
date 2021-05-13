while True:
    x = raw_input()
    if x == '0':break
    print sum(['0123456789'.index(c) for c in x])