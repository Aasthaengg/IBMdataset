# coding: utf-8
while True:
    n, x = map(int, input().split())
    comb = 0
    
    if n == 0 and x == 0:
        exit()

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                # print('{} {} {}'.format(i, j, k))
                if i + j + k == x:
                    comb += 1
    print(comb)

