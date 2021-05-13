# -*- coding: utf-8 -*-
import math

def main():

    A, B = input().split()

    A = int(A)
    B = float(B)

    ans = A * round(B * 100) // 100

    print(int(ans))


if __name__ == "__main__":
    main()