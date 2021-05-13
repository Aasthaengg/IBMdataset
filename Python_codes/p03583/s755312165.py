N = int(input())

for h in range(1, 3501):
    for n in range(h, 3501):
        a = N*h*n
        b = 4*h*n - N*n - N*h
        if not b:
            continue
        if a%b == 0 and a//b > 0:
            print(h, n, a//b)
            exit()