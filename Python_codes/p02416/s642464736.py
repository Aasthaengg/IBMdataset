while True:
    x = raw_input()
    if x == '0':
        break
    print sum(map(int , list(x)))