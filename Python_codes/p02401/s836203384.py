while True:
    s = raw_input()
    if s.split()[1] == '?':
        break
    print eval(s)