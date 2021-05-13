# coding=utf-8
import math

if __name__ == '__main__':
    A, B, C = map(int, input().split())

    MV = max(A, B, C) * 3
    SumABC = A + B + C

    if MV % 2 == 0 and SumABC % 2 == 0:
        ans = (MV - SumABC) / 2

    elif MV % 2 == 1 and SumABC % 2 == 1:
        ans = math.ceil(MV - SumABC) / 2

    else:
        ans = math.ceil((MV - SumABC) / 2) + 1

    print(int(ans))