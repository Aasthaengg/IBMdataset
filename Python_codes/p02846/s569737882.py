def p_f():
    t1, t2 = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())

    # aの方がt1のときに先行している
    if a1 < b1:
        a1, b1 = b1, a1
        a2, b2 = b2, a2

    dif1 = a1 * t1 - b1 * t1
    dif2 = (b1 * t1 + b2 * t2) - (a1 * t1 + a2 * t2)
    # print(dif1)
    # print(dif2)
    if dif2 < 0:
        print(0)
        exit()
    if dif2 == 0:
        print("infinity")
        exit()
    if dif1 % dif2 == 0:
        print(dif1 // dif2 * 2)
    else:
        print((dif1 + dif2) // dif2 * 2 - 1)
        
p_f()