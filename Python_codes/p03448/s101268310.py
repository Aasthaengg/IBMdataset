def resolve():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    count = 0
    n = 0
    for i in range(a+1):
        ni = 500*i
        if ni > x:
            continue
        for j in range(b+1):
            nj = ni + 100*j
            if nj > x:
                continue
            for k in range(c+1):
                nk = nj + 50*k
                if nk != x:
                    continue
                elif nk == x:
                    count += 1
    print(count)
resolve()