# -*- coding: utf-8 -*-
from math import floor

def solve():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())
    C1 = T1*(A1-B1)
    C = C1 + T2*(A2-B2)
    if C == 0:
        return 'infinity'
    elif C1/C > 0:
        return '0'
    elif C1/C > -1:
        return '1'
    else:
        res =  2*(floor(-C1/C)+1)-1-(C1/C).is_integer()
        return str(res)

if __name__ == '__main__':
    print(solve())
