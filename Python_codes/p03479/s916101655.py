#!/usr/bin/env python3


def main():
    # n = int(input())
    # i = list(map(int,input().split()))
    # j = list(map(int,input().split()))

    x, y = map(int, input().split())

    cnt = 0

    while True:
        cnt += 1
        x *= 2
        #print(x)
        if x > y:
            break

    print(cnt)

main()
