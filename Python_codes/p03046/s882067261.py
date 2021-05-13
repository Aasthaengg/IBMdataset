#!/usr/bin/env python3
import sys
INF = float("inf")


def main():
    M, K = map(int, input().split())

    # コーナーケース
    if M == 0:
        if K == 0:
            print("0 0")
        else:
            print("-1")
        return
    elif M == 1:
        if K == 0:
            print("0 0 1 1")
        else:
            print("-1")
        return

    # 一般
    if K >= (1 << M):
        print("-1")
        return

    # 実現可能ケース
    ans = []
    for i in range(1 << M):
        if i == K:
            continue
        ans.append(i)
    ans = ans[::-1] + [K] + ans + [K]
    print(" ".join(map(str, ans)))


if __name__ == '__main__':
    main()
