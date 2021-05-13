#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    a = list(map(int, input().split()))

    l = [0] * 9
    for i in range(N):
        n = a[i] // 400
        if n > 8:
            n = 8
        l[n] += 1

    ans_min = 0
    for i in range(8):
        if l[i] > 0:
            ans_min += 1



    gold = l[8]

    ans_max = ans_min
    ans_max += gold

    if ans_min == 0:
        ans_min = 1

    print(ans_min, ans_max)


if __name__ == '__main__':
    main()
