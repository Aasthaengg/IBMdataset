import sys
import math


def main(X=None):
    """
    >>> main(90)
    4
    >>> main(120)
    3
    >>> main(45)
    8
    >>> main(1)
    360
    >>> main(70)
    36
    """
    if not X:
        X = int(input())
    # q, r = divmod(360, X)
    # if r == 0:
    #     print(q)
    # ret = q
    # q, r = (X, r)
    # if r == 0:
    #     ret = ret * q + 1
    ret = 0
    cur = 0
    while True:
        ret += 1
        cur += X
        if cur % 360 == 0:
            print(ret)
            return


def _test():
    import doctest
    doctest.testmod()


USE_NUMBA = False
if USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE' or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'void(i8,i8)')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    if USE_NUMBA and sys.argv[-1] != '-p':
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import main  # pylint: disable=all
    elif sys.argv[-1] == "-t":
        _test()
        sys.exit()
    elif len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline

    # read parameter
    main()
