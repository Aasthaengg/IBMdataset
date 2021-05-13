#!/usr/bin/env pytHon3
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    A = list(map(int, input().split()))

    s = [A[0]]

    for i in range(1, N):
        s.append(s[-1] + A[i])

    cnt_a = 0
    base = 0
    for i in range(N):
        if ((base + s[i] >= 0) and (i % 2 == 1)) \
                or ((base + s[i] <= 0) and (i % 2 == 0)):
            cnt_a += (1 + abs(base + s[i]))
            base += (1 + abs(base + s[i])) * (-1) ** i

    cnt_b = 0
    base = 0
    for i in range(N):
        if ((base + s[i] <= 0) and (i % 2 == 1)) \
                or ((base + s[i] >= 0) and (i % 2 == 0)):
            cnt_b += (1 + abs(base + s[i]))
            base -= (1 + abs(base + s[i])) * (-1) ** i

    print(min(cnt_a, cnt_b))


if __name__ == "__main__":
    main()
