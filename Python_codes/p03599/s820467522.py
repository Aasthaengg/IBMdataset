A, B, C, D, E, F = map(int, input().split())

ans = [0, 0]
maxno = 0

a = 0
while True:
    aaa = 100*A*a
    if aaa > F:
        break

    b = 0
    while True:
        bbb = aaa+100*B*b
        if bbb > F:
            break
        
        c = 0
        while True:
            if not bbb:
                break
            ccc = C*c
            if ccc > F:
                break

            d = 0
            while True:
                ddd = ccc+D*d
                if bbb+ddd > F:
                    break

                if ddd/bbb > E/100:
                    break

                no = ddd / (bbb+ddd)

                if no >= maxno:
                    ans = [bbb+ddd, ddd]
                    maxno = no
                
                d += 1
            c += 1
        b += 1
    a += 1

print(*ans)