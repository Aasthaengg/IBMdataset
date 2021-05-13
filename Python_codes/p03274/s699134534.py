# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
"""
def main():
    N, K = map(int, input().split())
    x_lsit = list(map(int, input().split()))
    INF = pow(10, 9)

    min_time = INF
    for i in range(N-K+1):
        x_l = x_lsit[i]
        x_r = x_lsit[i+K-1]
        this_time = int()
        if x_l <= -1:
            if x_r <= 0:
                this_time = -x_l
            else:
                this_time = min(-x_l, x_r)*2 + max(-x_l, x_r)
        else:
            this_time = x_r
        min_time = min(min_time, this_time)
    print(min_time)
    return

if __name__ == "__main__":
    main()

