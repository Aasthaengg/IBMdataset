while True:
    s = input()
    if int(s) == 0:
        break
    g  = 0
    for c in s:
        g += int(c)
    print(g)