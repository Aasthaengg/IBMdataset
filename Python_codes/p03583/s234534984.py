N = int(input())
for i in range(1, 3501):
    for j in range(1, 3501):
        a, b = N*i*j,  4*i*j-(i+j)*N
        if b > 0 and a % b == 0:
            print(i, j, a // b)
            exit()