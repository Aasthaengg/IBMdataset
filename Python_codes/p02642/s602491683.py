import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
from numba import njit
def main():

    @njit
    def solve(a):
        count = np.zeros(10 ** 6 + 1, np.int32)
        for ae in a:
            if count[ae] <= 1:
                count[::ae] += 1
        r = 0
        for ae in a:
            r += count[ae] == 1
        return r

    a = np.array(read().split(), np.int32)[1:]
    print(solve(a))

if __name__ == '__main__':
    main()
