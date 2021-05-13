#!/usr/bin/env python3

import math

def main():
    n = int(input())

    div = n/1.08
    fl = math.floor(div)
    if math.floor(fl*1.08) == n:
        print(fl)
    elif math.floor((fl+1)*1.08) == n:
        print(fl+1)
    else:
        print(":(")


if __name__ == '__main__':
    main()