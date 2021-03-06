# -*- coding: utf-8 -*-
import sys
from decimal import Decimal, ROUND_HALF_UP


def main():
    N,K = list(map(int, sys.stdin.readline().split()))
    A_list = list(map(int, sys.stdin.readline().split()))


    def check(length :int) -> bool:
        cnt = 0

        for a in A_list:
            if a >= length:
                quotient = a / length
                divide = -(-quotient // 1)  # round up
                cnt += (divide - 1)
        
        return (True if cnt <= K else False)


    L = 0            # the minimum length
    R = max(A_list)  # the maximum length

    while (R - L) > 1:
        M = L + (R - L) // 2

        if check(M):
            R = M
        else:
            L = M


    print(R)


if __name__ == "__main__":
    main()
