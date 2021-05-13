# -*- coding: utf-8 -*-

import math

def main():

    H, A = map(int, input().split())

    ans = math.ceil(H / A)

    print(ans)


if __name__ == "__main__":
    main()