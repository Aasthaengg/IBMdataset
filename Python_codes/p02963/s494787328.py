#!/usr/bin/env python

def main():
    s = int(input())
    if s <= 10 ** 9:
        x1 = s
        y2 = 1
        y1 = 0
        x2 = 0
    elif s < 10 ** 18:
        u, d = divmod(s, 10**9)
        x1 = u + 1
        y2 = 10 ** 9
        y1 = 10 ** 9 - d
        x2 = 1
    else:
        x1 = 10 ** 9
        y2 = 10 ** 9
        y1 = 0
        x2 = 0

    print(0, 0, x1, y1, x2, y2)

if __name__ == '__main__':
    main()
