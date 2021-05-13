# -*- coding: utf-8 -*-
import math

def main():

    A, B, C, D = map(int, input().split())

    t = math.ceil(A / D)
    a = math.ceil(C / B)

    if t >= a:
        ans = 'Yes'

    else:
        ans = 'No'


    print(ans)


if __name__ == "__main__":
    main()