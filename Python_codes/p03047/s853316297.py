from io import StringIO
from collections import *
from functools import *
import sys


def main(inputs):
    #n = int(next(inputs))
    # xs = list(map(int, next(inputs).split()))
    n, k = map(int, next(inputs).split())
    return n - k + 1


def gen_inputs(str_=None):
    inputs = StringIO(str_) if str_ else sys.stdin
    while True:
        a = inputs.readline().rstrip()
        yield a
        pass
    pass


if __name__ == "__main__":
    print(main(gen_inputs()))
    pass
