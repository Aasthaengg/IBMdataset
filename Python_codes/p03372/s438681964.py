#!/usr/bin/env python3

def main():
    na = list(map(int, input().split()))
    N, C = na[0], na[1]
    x, v = [], []
    for i in range(N):
        na = list(map(int, input().split()))
        x.append(na[0])
        v.append(na[1])

    cw1 = [0] * N
    cw2 = [0] * N
    acw1 = [0] * N
    acw2 = [0] * N

    sum_v = 0
    m1 = m2 = 0
    for i in range(N):
        sum_v += v[i]
        m1 = max(m1, sum_v - x[i])
        cw1[i] = m1
        m2 = max(m2, sum_v - x[i] * 2)
        cw2[i] = m2

    sum_v = 0
    m1 = m2 = 0
    for i in range(N - 1, -1, -1):
        sum_v += v[i]
        m1 = max(m1, sum_v - (C - x[i]))
        acw1[i] = m1
        m2 = max(m2, sum_v - (C - x[i]) * 2)
        acw2[i] = m2

    m = max(cw1[N - 1], acw1[0])
    for i in range(N - 1):
        m = max(m, cw1[i] + acw2[i + 1], cw2[i] + acw1[i + 1])

    print(m)


if __name__ == '__main__':
    main()

