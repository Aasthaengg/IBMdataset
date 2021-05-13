a = True
while a:
    l = list(map(int, list(input())))
    if l[0] != 0:
        print(sum(l))
    else:
        a = False
