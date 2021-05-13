while 1:
    try:
        a, b = map(int, raw_input().split())
        if a > b: x, y = a, b
        else: x, y = b, a

        r = x % y
        while (r != 0):
            x = y
            y = r
            r = x % y
        gcd = y

        lcm = (a / gcd) * b

        print str(gcd) + " " + str(lcm)

    except:
        break