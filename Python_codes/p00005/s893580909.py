# -*- coding: utf-8 -*-
while True:
    try:
        list = [int(x) for x in raw_input().split(" ")]
        list.sort(lambda x, y: y - x)
        gcd = lcm = 0
        m = list[0]
        n = list[1]
        while True:
            r = m%n
            if r == 0:
                gcd = n
                break
            m = n
            n = r
        lcm = list[0] * list[1] / gcd
        print(str(gcd) + " " + str(lcm))
    except EOFError:
        break