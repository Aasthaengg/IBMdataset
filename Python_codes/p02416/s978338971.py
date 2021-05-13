while(True):
    s = input()
    if s == '0': exit()
    print(sum([int(c) for c in s]))