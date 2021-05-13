
import itertools

def solve(T,X):
    """
    >>> solve(8,3)
    2.6666666667
    """
    print(T/X)


def main():
    T,X = map(int,input().split())
    solve(T,X)


def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    import sys
    argv = sys.argv
    if len(sys.argv) == 1:
        # no option
        main()
    elif sys.argv[1] == "-t":
        _test()
    else:
        input = open(sys.argv[1]).buffer.readline