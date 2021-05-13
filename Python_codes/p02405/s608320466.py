while True:
    n = input().split()
    h = int(n[0])
    w = int(n[1])
    switch = 0
    switch2 = 1
    if h == 0 and w == 0:
        break
    for i in range(h):
        line = ''
        if switch2:
            switch = 0
            switch2 = 0
        else:
            switch = 1
            switch2 = 1
        for j in range(w):
            if switch == 0:
                line += '#'
                switch = 1
            else:
                line += '.'
                switch = 0
        print(line)
        

    print()