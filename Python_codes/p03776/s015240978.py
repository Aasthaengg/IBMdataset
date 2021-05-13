import numpy as np
import copy
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0 or r == n: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under



def main():
    N, A, B = map(int, input().split())

    v = list(map(int, input().split()))

    v = np.sort(v)[::-1]
    ave_max = np.mean(v[:A])

    print(ave_max)


    m = np.sum(v > v[A-1])
    n = np.sum(v == v[A-1])

    if m > 0:
        print(cmb(n, A-m))
    else:
        ans = 0
        for k in range(A, min(B, n)+1):
            ans += cmb(n, k)
        print(ans)


if __name__ == '__main__':
    main()
