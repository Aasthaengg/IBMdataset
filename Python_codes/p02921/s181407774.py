#!/usr/bin/env python3

def main():
    S, T = map(str, open(0).read().split())
    cnt = 0

    for i in range(0, 3):
        if S[i] == T[i]:
            cnt += 1

    print(cnt)


main()