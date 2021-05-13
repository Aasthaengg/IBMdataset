N = int(input())
ok = False

for i in range(1, 3501):
    for j in range(1, 3501):
        if N*(i+j) < 4*i*j:
            w = 1 / (4/N - 1/i - 1/j)
            if abs(int(w)-w) < 10**-7:
                print(i, j, int(w))
                ok = True
                break
    if ok:
        break