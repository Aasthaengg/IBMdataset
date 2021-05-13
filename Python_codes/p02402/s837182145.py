# -*- coding: utf-8 -*-

def calc(list):
    """
    return (min,max,sum)

    >>> calc([10, 1, 5, 4, 17])
    (1, 17, 37)
    >>> calc([-2, -1, 0])
    (-2, 0, -3)
    >>> calc([-1000000,1000000,0])
    (-1000000, 1000000, 0)
    """

    return (min(list),max(list),sum(list))


if __name__ == '__main__':
    n = int(raw_input())
    list = map(int,raw_input().split())
    print " ".join(map(str,calc(list)))