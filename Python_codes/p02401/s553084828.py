while(True):
    f = input()
    s = f.split()
    if(s[1] == '?'):
        break
    if(s[1] == '/'):
        print((int)(s[0]) // (int)(s[2]))
    else:
        print(eval(f))
