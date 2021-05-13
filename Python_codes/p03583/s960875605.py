import sys
N = int(input())
for h in range(1, 3501):
    Nh = N*h
    for n in range(1, 3501):
        Nn = N * n
        left = 4*h*n - Nn - Nh
        Nhn = N * n * h
        if left > 0 and Nhn % left == 0:
            print(h, n, Nhn // left)
            sys.exit()