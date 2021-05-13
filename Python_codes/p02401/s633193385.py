while 1:
    x = raw_input()
    i = x.split()
    if i[1]=="?": break
    print eval(x)