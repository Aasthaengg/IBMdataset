#!/usr/bin/env python3
def main():
    N, M = map(int, input().split())
    num = [-1] * N
    for _ in [0] * M:
        s, c = map(int, input().split())
        if num[s - 1] == -1 or num[s - 1] == c:
            num[s - 1] = c
        else:
            print(-1)
            return
    if num[0] == 0 and len(num) != 1:
        print(-1)
        return
    if num[0] == -1 and len(num) != 1:
        num[0] = 1
    for x in num:
        print(0 if x == -1 else x, end='')


if __name__ == '__main__':
    main()
