import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
   CCC
   CAtD
   CABD
   CsBD
    DDD

    UUR
    DDL
    LUUURRD
    RDDDLLU

    """
    sx, sy, tx, ty = read_ints()
    return 'U'*(ty-sy)+'R'*(tx-sx)+'D'*(ty-sy)+'L'*(tx-sx)+'L'+'U'*(ty-sy+1)+'R'*(tx-sx+1)+'D'+'R'+'D'*(ty-sy+1)+'L'*(tx-sx+1)+'U'


if __name__ == '__main__':
    print(solve())
