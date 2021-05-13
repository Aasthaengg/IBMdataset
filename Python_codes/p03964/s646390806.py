#!/usr/bin/env python3
import sys
INF = float("inf")


def main():
    # i回目 Ti : Ai
    N = int(input())
    T, A = [], []
    for i in range(N):
        t, a = map(int, input().split())
        T.append(t)
        A.append(a)

    num = [0, 0]
    for i, (t, a) in enumerate(zip(T, A)):
        # print(i, t, a, num)
        while True:
            if num[0] <= t and num[1] <= a:
                break
            if num[0] <= t:
                # print("B", t, a, num)
                c = -(-num[1]//a)
                a *= c
                t *= c
                continue
            if num[1] <= a:
                # print("C", t, a, num)
                c = -(-num[0]//t)
                199, 17
                a *= c
                t *= c
                continue
            c = max(-(-num[0]//t), -(-num[1]//a))
            # print("D", t, a, num, c)
            a *= c
            t *= c
            continue
        num[0] = t
        num[1] = a
        # print(a, t)
    print(num[0]+num[1])


if __name__ == '__main__':
    main()
