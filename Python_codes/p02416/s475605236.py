while True:
    x = input()
    if int(x) == 0:break
    ret = 0
    for a in x:
        ret += int(a)
    print(ret)