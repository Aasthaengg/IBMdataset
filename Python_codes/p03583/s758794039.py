# -*- coding: utf-8 -*-
N = int(input())


for h in range(1, 3500+1):
    for w in range(1, 3500 + 1):
        n1 = 4*h*w - h*N - w*N
        if n1:
            l = (h*w*N) / n1
            if 0 < l <= 3500 and int(l) == l:
                print(int(h), int(l), int(w))
                exit()
