n = int(input())
stop = False
for a in range(1, 3501):
    if stop:
        break
    for b in range(1, 3501):
        p = (n*a*b)
        q = 4*a*b - n*a - n*b
        if q > 0:
            r, s = divmod(p, q)
        
            if s == 0 and r > 0:
                print(a, b, r)
                stop = True
                break
