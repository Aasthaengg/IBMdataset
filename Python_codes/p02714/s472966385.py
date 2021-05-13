import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
from numba import njit
def main():
    n = int(input())
    s = np.array(list(read().rstrip()))

    r = np.sum(s == 'R')
    g = np.sum(s == 'G')
    b = np.sum(s == 'B')
    @njit
    def f(s):
        ret = 0
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                i3 = i2 * 2 - i1
                if i3 <= n - 1:
                    if s[i1] != s[i2] and s[i1] != s[i3] and s[i2] != s[i3]:
                        ret += 1
        return ret

    res = r * g * b - f(s)
    print(res)

if __name__ == '__main__':
    main()
