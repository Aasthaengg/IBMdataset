n = int(input())
if n == 1:
    print(1)
else:
    Li = 2
    Lj = 1
    cnt = 2
    while True:
        Lk = Li + Lj
        if cnt == n:
            print(Lk)
            break
        cnt += 1
        Li = Lj
        Lj = Lk