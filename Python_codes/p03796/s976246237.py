# -*- coding: utf-8 -*-

import math

def main():

    N = int(input())

    ans = math.factorial(N)

    ans %= (10 ** 9 + 7)

    print(ans)


if __name__ == "__main__":
    main()