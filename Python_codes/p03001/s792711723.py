#!/usr/bin/env python3


def main():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    multi = int((x == W / 2) and (y == H / 2))

    print(area, multi)


if __name__ == '__main__':
    main()
