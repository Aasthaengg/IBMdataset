# -*- coding: utf-8 -*-

import math

def main():

    N, D = map(int, input().split())

    ans = math.ceil(N / (2 * D + 1))

    print(ans)


if __name__ == "__main__":
    main()