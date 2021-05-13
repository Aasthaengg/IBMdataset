# coding: utf-8
N = int(input())
for h in range(1, 3501)[::-1]:
    for n in range(1, 3501)[::-1]:
        if 4*h*n-N*(h+n) == 0:
            continue
        w = (N*(h*n)) / (4*h*n-N*(h+n))
        if w != int(w) or w <= 0:
            continue
        w = int(w)
        if 4/N == (n*w+h*w+h*n)/(h*n*w):# and 1 <= h <= 3500 and 1 <= n <= 3500 and 1 <= w <= 3500:
            print(h, n, w)
            exit()