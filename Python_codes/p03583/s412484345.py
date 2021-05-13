N = int(input())

for a in range(1,3501):
    for b in range(1,3501):
        x = a*b*N
        y = 4*a*b - b*N - a*N
        if y != 0 and x/y > 0:
            c = x//y
            if 4*a*b*c == b*c*N + a*c*N + a*b*N:
                print(a,b,c)
                exit()